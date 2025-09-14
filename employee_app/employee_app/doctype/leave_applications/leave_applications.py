#calculate leave balance on submission of leave application
import frappe
from frappe.model.document import Document
from datetime import datetime


class LeaveApplications(Document):
	def on_submit(self):
		if self.status == "Approved":
			leave_days = (frappe.utils.getdate(self.to_date) - frappe.utils.getdate(self.from_date)).days + 1
			lb_name = frappe.db.get_value("Leave Balances", {"employee": self.employee}, "name")
			if lb_name:
				balance = frappe.get_doc("Leave Balances", lb_name)
				balance.reload()
				balance.leaves_taken = (balance.leaves_taken or 0) + leave_days
				balance.leave_balance = (balance.total_leaves or 0) - (balance.leaves_taken or 0)
				frappe.msgprint(f"Before Save: leave_balance={balance.leave_balance}, leaves_taken={balance.leaves_taken}")
				balance.save()
				frappe.db.commit()
				frappe.msgprint(f"After Save: leave_balance={balance.leave_balance}, leaves_taken={balance.leaves_taken}")
				self.db_set("leave_balance", balance.leave_balance)

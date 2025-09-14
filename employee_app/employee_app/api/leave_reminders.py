import frappe
def send_pending_leave_reminders():
    pending_apps = frappe.get_all("Leave Applications", filters={"status": "Pending"}, fields=["name", "employee", "from_date", "to_date"])
    for app in pending_apps:
        approver_email = "nivithamerlin@gmail.com"
        frappe.sendmail(
            recipients=[approver_email],
            subject="Pending Leave Approval Reminder",
            message=f"""
                 Leave Application {app.name} is still pending.
                 Employee: {app.employee}
                 From: {app.from_date} To: {app.to_date}
                 Please review and approve.
                 """

        )
def send_weekly_pending_summary():
    pending_apps = frappe.get_all("Leave Applications",
        filters={"status": "Pending"},
        fields=["employee", "from_date", "to_date"])
    print("Pending apps found:", pending_apps)
    if not pending_apps:
        return
    message = "<h3>Pending Leave Applications</h3><ul>"
    for app in pending_apps:
        message += f"<li>{app.employee}: {app.from_date} → {app.to_date}</li>"
    message += "</ul>"

    frappe.sendmail(
        recipients=["nivithamerlin@gmail.com"],  
        subject="Weekly Pending Leave Applications",
        message=message
    )


    
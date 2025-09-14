// Copyright (c) 2025, Nivitha and contributors
// For license information, please see license.txt
//auto fetch leave balance in leave application form
frappe.ui.form.on("Leave Applications", {
    employee: function(frm) {
        if (frm.doc.employee) {
            frappe.db.get_value('Leave Balances', { employee: frm.doc.employee }, 'leave_balance')
                .then(r => {
                    if (r && r.message) {
                        frm.set_value('leave_balance', r.message.leave_balance);
                        frappe.msgprint("Leave balance autofilled: " + r.message.leave_balance);
                    }
                });
        }
    },
  
// validation to avoid overlapping leave applications on same date which are already approved
    validate: function(frm) {
        if (frm.doc.from_date && frm.doc.to_date && frm.doc.employee) {
            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: "Leave Applications",
                    filters: [
                        ["employee", "=", frm.doc.employee],
                        ["status", "=", "Approved"],
                        ["from_date", "<=", frm.doc.to_date],
                        ["to_date", ">=", frm.doc.from_date]
                    ],
                    fields: ["employee", "from_date", "to_date"]
                },
                callback: function(r) {
                    if (r.message && r.message.length > 0) {
                        frappe.msgprint(
                            __("This leave overlaps with another approved leave from {0} to {1}",
                            [r.message[0].from_date, r.message[0].to_date])
                        );
                        frappe.validated = false; 
                    }
                }
            });
        }
    }
});
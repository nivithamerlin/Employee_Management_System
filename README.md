
---

# 👩‍💼 Employee Management System – README.md
```markdown
# Employee Management System

A Frappe-based application to manage **employees, leave applications, and leave records** for organizations.

---

## 🚀 Features
- **Employee Management**
  - Store employee details (ID, name, email, date of joining, status)
  - Validations (e.g., no future date of joining, unique employee ID)
  - Company email check (`@company.com`

- **Leave Applications**
  - Submit leave requests with from-date and to-date
  - Prevent overlapping approved leaves
  - Auto-update leave balances when approved

- **Workflows**
  - Leave Application: Pending → Approved → Rejected
  - Membership Renewal (example workflow)

- **API Endpoints**
  - Fetch employee list
  - Update attendance via API (usable in Postman)

---

## 🛠 Tech Stack
- [Frappe Framework](https://frappeframework.com) v15
- Python 3.x
- MariaDB / MySQL
- Redis
- Node.js

---


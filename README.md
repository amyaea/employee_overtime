# employee_overtime
This Odoo module is used to manage employees requests for overtime
# Employee Overtime Management (Odoo 17)

A custom Odoo module for managing employee overtime requests with role-based access and approval workflows.

---

## 🚀 Features
- Employees can:
  - Submit overtime requests (date, hours, reason).
  - View only their own requests.
- Managers can:
  - Approve / Reject overtime requests.
  - View all employee requests (except drafts).
- Automated status workflow: **Draft → Submitted → Approved / Rejected**.
- Role-based access:
  - **Overtime Employee**: limited access, own requests only.
  - **Overtime Manager**: approval rights, full visibility.
- Custom search filters:
  - Today, Tomorrow, Next Week, Next Month.
- Employee auto-linking to the logged-in user.

---

## 🛠️ Tech Stack
- **Odoo 17**
- **Python (Odoo ORM)**
- **XML (Views, Menus, Actions)**
- **PostgreSQL**
- **Git & GitHub**

---

## 📂 Module Structure

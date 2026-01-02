{
    'name': 'Employee Overtime Management',
    'version': '1.0',
    'category': 'Human Resources',
    'author' : 'Ahmed Abdelgadir',
    'summary': 'Employee overtime request and approval workflow',
    'depends': ['base', 'mail'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/employee_profile_view.xml',
        'views/employee_overtime_view.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True
}
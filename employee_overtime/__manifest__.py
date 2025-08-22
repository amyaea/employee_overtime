{
    'name': 'Employee Overtime Management',
    'version': '1.0',
    'category': 'Human Resources',
    'author' : 'Benjamin',
    'summary': 'This module is used to manage employees requests for overtime',
    'sequence': 1,
    'depends': [],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'data/employee_details_data.xml',
        'views/employee_overtime_view.xml'
    ],
    'installable': True,
    'application': True,
}
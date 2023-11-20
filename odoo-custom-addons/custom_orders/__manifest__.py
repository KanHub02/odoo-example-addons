{
    'name': 'Custom Orders',
    'version': '1.0',
    'summary': 'Custom Module for Managing Orders',
    'sequence': -100,
    'description': """Custom Module for Managing Orders""",
    'category': 'Sales',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # "views/actions.xml",
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

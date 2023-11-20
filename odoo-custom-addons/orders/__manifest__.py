{
    'name': 'My Order Module',
    'version': '1.0',
    'summary': 'Order Creation Module',
    'sequence': 10,
    'description': "Custom module to create orders",
    'category': 'Sales',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/order_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

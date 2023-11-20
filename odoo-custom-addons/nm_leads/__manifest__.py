# -*- coding: utf-8 -*-
{
    'name': "nm_leads",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Кастомные Лиды
    """,

    'author': "Self",
    'website': "https://kanhub02.github.io/",
    'category': 'Sales/CRM',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
        "views/menu.xml",
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

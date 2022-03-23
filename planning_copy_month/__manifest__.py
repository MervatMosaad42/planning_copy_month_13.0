# -*- coding: utf-8 -*-
{
    'name': "planning_copy_month",

    'summary': """Copy Previous Month of planning enterprise edition""",

    'description': """
       Copy Previous Month Button to copy all planning data in previous month
    """,

    'author': "Mervat Mosaad",
    'website': "mervatmosaad96@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'planning', 'web_gantt', 'web'],

    # always loaded
    'data': [
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        'static/src/xml/planning_gantt.xml',
    ],
    'application': True,

    'license': 'OEEL-1',
}

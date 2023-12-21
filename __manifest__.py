# -*- coding: utf-8 -*-
{
    'name': "modulo copado",

    'summary': """
                un pequenio modulo copado que hace cosas copadas
                """,

    'description': """
        un pequenio modulo copado que hace cosas copadas como por ejemplo algo especifico que te vuela el cerebro de lo copado y especifico que es.
        
    """,

    'author': "tenache89",
    'website': "https://github.com/tenache",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':  'Chatbot',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views_products.xml',
        # 'views/views_try.xml',
        'views/clothes_types_view.xml',
        'views/views_storage.xml',
        'views/views_sale_order.xml'
        # 'views/views.xml',
        # 'views/templates.xml',
        # 'reports/visit.xml'
    ],
    'application': True
}

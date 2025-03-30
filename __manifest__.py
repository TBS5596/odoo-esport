# -*- coding: utf-8 -*-
{
    'name': "Banks ZM",

    'summary': "Bank Ext.",

    'description': """
    Banking Extension for Zambia
    """,

    'author': "ISWE Solutions Limited",
    'website': "https://www.iswesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/res_bank.xml',
        'data/res_bank_zanaco.xml',
        'data/res_bank_natsave.xml',
        'data/res_bank_stanbic.xml',
        'data/res_bank_uba.xml',
        'data/res_bank_indo.xml',
        'data/res_bank_fnb.xml',
        'views/res_bank.xml'
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': "LGPL-3",
}
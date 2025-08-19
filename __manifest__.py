# -*- coding: utf-8 -*-
{
    'name': "eSport",
    'summary': "Gaming Module",
    'description': """
    Gaming Module for Odoo
    """,
    'author': "Thom Simbeye",
    'category': 'Customizations',
    'version': '18.0',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/player.xml',
        'views/esport_menu.xml',
    ],
    'demo': [],
    'images': ['static/description/team.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': "LGPL-3",
}

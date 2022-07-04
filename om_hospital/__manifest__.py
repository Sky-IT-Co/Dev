# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Hussain Ali',
    'sequence': '-100',
    'summary': 'This hospital demo',
    'description': """
This hospital demo
    """,
    'depends': [],
    'data': [ 
        'security/ir.model.access.csv',
        'views/menu.xml' ,
        'views/patient_menu.xml' 
      ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {    },
    'license': 'LGPL-3',
}

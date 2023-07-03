# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': 'TH: Tags',
    'version': '1.0.',
    'category': 'Other',
    'license': '',
    'author': 'Tecnihand',
    'website': 'https://www.tecnihand.com',
    'maintainer': 'Joel Estrada',
    'summary': """Módulo Tags""",
    'depends': ["sale"],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_tag_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
}

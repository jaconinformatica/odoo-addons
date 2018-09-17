# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Business Areas',
    'summary': 'Business Areas information for invoice',
    'author': 'Jacon',
    'license': 'AGPL-3',
    'website': 'http://www.jacon.es',
    'category': 'Accounting',
    'version': '8.0.1.0.0',
    'depends': [
        'account',
        'base_view_inheritance_extension'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_business_areas.xml',
        'views/account_move.xml',
        'views/account_move_line.xml',
        'views/account_invoice.xml',
        'views/account_invoice_report.xml',
    ],
    'installable': True,
}

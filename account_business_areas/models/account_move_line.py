# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    business_area_id = fields.Many2one(
        'account.business.areas',
        index=True,
        string='Area de negocio'
    )

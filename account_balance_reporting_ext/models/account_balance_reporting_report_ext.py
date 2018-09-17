# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).

from openerp import fields, models

class AccountBalanceReporting(models.Model):
    _inherit = 'account.balance.reporting'

    title = fields.Char(string='Title', required=False, index=False)
    description = fields.Text(string='Description', required=False, index=False)

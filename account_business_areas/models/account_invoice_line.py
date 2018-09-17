# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.model
    def _default_business_area(self):
        return self.env['account.business.areas'].browse(
            self._context.get('business_area_id'))

    business_area_id = fields.Many2one(
        'account.business.areas',
        string='Area de negocio',
        index=True,
        default=_default_business_area
    )

    @api.model
    def move_line_get_item(self, line):
        res = super(AccountInvoiceLine, self).move_line_get_item(line)
        if line.business_area_id:
            res['business_area_id'] = line.business_area_id.id
        return res

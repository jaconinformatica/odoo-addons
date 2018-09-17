# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    business_area_id = fields.Many2one(
        'account.business.areas',
        string='Area de negocio',
        readonly=True
    )
    account_analytic_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        readonly=True
    )

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + \
            ", sub.business_area_id as business_area_id, " + \
            "sub.account_analytic_id as account_analytic_id"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() + \
            ", ail.business_area_id as business_area_id, " + \
            "ail.account_analytic_id as account_analytic_id"

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + \
            ", ail.business_area_id, " + \
            "ail.account_analytic_id"

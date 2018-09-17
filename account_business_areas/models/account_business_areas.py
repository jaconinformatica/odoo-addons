# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class AccountBusinessAreas(models.Model):
    _name = 'account.business.areas'
    _description = 'Account Business Areas'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)
    description = fields.Text(string='Descripción', required=False)
    company_id = fields.Many2one(
            comodel_name='res.company',
            string='Company',
            required=True,
            default=lambda self: self.env.user.company_id
            )

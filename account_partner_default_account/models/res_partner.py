# Copyright 2017-2019 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_default_account_id = fields.Many2one(
        'account.account',
        company_dependent=True,
        domain="[('internal_type', 'not in', ('receivable', 'payable')), ('deprecated', '=', False)]",
        string="Partner Default Account",
    )

    @api.onchange('company_id', 'partner_default_account_id')
    def onchange_default_account_company(self):
        if self.env.context.get('skip_default_account_company_check'):
            return
        msg = _("The Company in Partner Default Account is "
                "different that the one of the Partner.")
        warning_msg = {
            'title': _('Warning!'),
            'message': msg,
        }
        if self.company_id and self.partner_default_account_id:
            if self.company_id != self.partner_default_account_id.company_id:
                return {'warning': warning_msg, }

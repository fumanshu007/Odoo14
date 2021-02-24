# Copyright 2017-2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _get_computed_account(self):
        partner = self.move_id.partner_id
        if partner:
            if not self.move_id.is_invoice():
                pass
            elif not partner.partner_default_account_id:
                pass
            elif partner.partner_default_account_id:
                company_acc = partner.partner_default_account_id.company_id
                if partner.company_id == company_acc or not partner.company_id:
                    return partner.partner_default_account_id
        return super()._get_computed_account()

    @api.model
    def default_get(self, default_fields):
        values = super().default_get(default_fields)

        if 'account_id' in default_fields and values.get('partner_id'):
            # Override 'account_id'.
            partner = self.env['res.partner'].browse(values.get('partner_id'))
            if partner.partner_default_account_id:
                values['account_id'] = partner.partner_default_account_id.id

        return values

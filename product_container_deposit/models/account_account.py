from odoo import api, fields, models


class AccountAccount(models.Model):
    _inherit = 'account.account'

    is_container_deposit = fields.Boolean(
        string='Container Deposit'
    )

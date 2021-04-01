# Copyright 2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = ["res.company", "sendcloud.onboarding.mixin"]

    sendcloud_integration_ids = fields.One2many(
        "sendcloud.integration", "company_id", string="SendCloud Integrations"
    )
    sendcloud_brand_ids = fields.One2many(
        "sendcloud.brand", "company_id", string="SendCloud Brands"
    )
    sendcloud_return_ids = fields.One2many(
        "sendcloud.return", "company_id", string="SendCloud Returns"
    )
    sendcloud_invoice_ids = fields.One2many(
        "sendcloud.invoice", "company_id", string="SendCloud Invoices"
    )
    sendcloud_sender_address_ids = fields.One2many(
        "sendcloud.sender.address", "company_id", string="SendCloud Sender Addresses"
    )

    sendcloud_default_integration_id = fields.Many2one(
        "sendcloud.integration", compute="_compute_sendcloud_default_integration_id"
    )

    is_sendcloud_test_mode = fields.Boolean()

    @api.depends(
        "sendcloud_integration_ids.public_key",
        "sendcloud_integration_ids.secret_key",
        "sendcloud_integration_ids.sequence",
    )
    def _compute_sendcloud_default_integration_id(self):
        for company in self:
            integrations = company.sendcloud_integration_ids
            integrations = integrations.filtered(
                lambda i: i.public_key and i.secret_key
            ).sorted(key=lambda i: i.sequence)
            company.sendcloud_default_integration_id = fields.first(integrations)

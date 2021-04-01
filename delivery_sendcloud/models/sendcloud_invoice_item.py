# Copyright 2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SendCloudInvoice(models.Model):
    _name = "sendcloud.invoice.item"
    _description = "SendCloud Invoice Items"

    name = fields.Char()
    sendcloud_code = fields.Integer(required=True)
    sendcloud_invoice_id = fields.Many2one("sendcloud.invoice", ondelete="cascade")

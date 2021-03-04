from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    container_deposit_product_id = fields.Many2one(
        comodel_name='product.product',
        related='product_id.container_deposit_product_id'
    )

    price_container_deposit = fields.Monetary(
        string='Container Deposit',
        compute='_compute_container_deposit',
        store=True
    )

    @api.depends('container_deposit_product_id', 'quantity')
    def _compute_container_deposit(self):
        for line in self:
            line.price_container_deposit = line.container_deposit_product_id.list_price * line.quantity

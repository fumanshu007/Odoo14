from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    container_deposit_product_id = fields.Many2one(
        comodel_name='product.product',
        related='product_id.container_deposit_product_id'
    )

    price_container_deposit = fields.Monetary(
        string='Container Deposit',
        compute='_compute_container_deposit',
        store=True
    )

    @api.depends('container_deposit_product_id', 'product_uom_qty')
    def _compute_container_deposit(self):
        for line in self:
            line.price_container_deposit = line.container_deposit_product_id.list_price * line.product_uom_qty

    @api.depends('price_container_deposit')
    def _compute_amount(self):
        super()._compute_amount()
        for line in self:
            line.price_total = line.price_total + line.price_container_deposit

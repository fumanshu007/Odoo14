from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_container_deposit = fields.Monetary(
        compute='_amount_all',
        string='Container Deposit'
    )

    def _amount_all(self):
        super()._amount_all()
        for order in self:
            total_container_deposit = 0.0
            for line in order.order_line:
                total_container_deposit += line.price_container_deposit
            order.update({
                'total_container_deposit': total_container_deposit,
                'amount_total': order.amount_total + total_container_deposit
            })

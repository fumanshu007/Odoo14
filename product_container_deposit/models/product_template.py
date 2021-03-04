from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    container_deposit_product_id = fields.Many2one(
        comodel_name='product.product',
        string='Container-deposit Product'
    )

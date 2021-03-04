from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    total_container_deposit = fields.Monetary(
        string='Container Deposit',
        compute='_compute_container_deposit',
        store=True
    )

    @api.depends('invoice_line_ids.price_container_deposit')
    def _compute_container_deposit(self):
        for move in self:
            move.total_container_deposit = sum(move.invoice_line_ids.mapped('price_container_deposit'))

    @api.depends('total_container_deposit')
    def _compute_amount(self):
        super()._compute_amount()
        for move in self:
            if move.move_type == 'out_invoice':
                move.amount_total += move.total_container_deposit

    def _recompute_payment_terms_lines(self):
        super()._recompute_payment_terms_lines()
        if self.move_type == 'out_invoice':
            container_depo_line = self.line_ids.filtered(lambda l: l.account_id.is_container_deposit)
            receivable = self.line_ids.filtered(lambda l: l.account_id.user_type_id.type == 'receivable')
            if container_depo_line:
                receivable.debit -= container_depo_line.credit
                container_depo_line.credit = self.total_container_deposit
                receivable.debit += container_depo_line.credit
            else:
                receivable.debit += self.total_container_deposit
                container_depo_account = self.env['account.account'].search([
                    ('is_container_deposit', '=', True),
                    ('company_id', '=', self.company_id.id),
                    ('deprecated', '=', False)
                ], limit=1)
                if not container_depo_account:
                    raise UserError(_('No Deposit Container account configured.'))
                self.write({'line_ids': [(0, 0, {
                    'account_id': container_depo_account.id,
                    'name': 'Container Deposit',
                    'debit': 0,
                    'credit': self.total_container_deposit,
                    'exclude_from_invoice_tab': True
                })]})

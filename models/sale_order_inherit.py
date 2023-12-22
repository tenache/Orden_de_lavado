from odoo import models, fields, api, _

class SaleOrderLaundryInherit(models.Model):
    _inherit = 'sale.order'
    _description = 'DESC AQUI'
    
    place_id = fields.Many2one(comodel_name="tenache89.clothes.places")
    
    state_display = fields.Char(compute='_compute_state_display')
    
    def _compute_state_display(self):
        for record in self:
            if record.state == 'draft':
                record.state_display = 'Por lavar'
            elif record.state == 'sale':
                record.state_display = 'Por entregar'
            elif record.state == 'done':
                record.state_display = 'Entregado'
            else:
                record.state_display = record.state
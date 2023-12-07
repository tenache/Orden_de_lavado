from odoo import models, fields, api, _


class SaleOrderLaundryInherit(models.Model):
    _inherit = 'sale.order'
    _description = 'DESC AQUI'
    
    place_id = fields.Many2one(comodel_name="tenache89.clothes.places")
    
from odoo import models, fields, api, _

class SaleOrderLineLaundryInherit(models.Model):
    _inherit = 'sale.order.line'
    _description = 'DESC AQUI'
    
    clothes_types = fields.Many2one(comodel_name='tenache89.clothes.types')
    clothes_brands = fields.Many2one(comodel_name='tenache89.clothes.brands')
    clothes_sizes = fields.Many2one(comodel_name='tenache89.clothes.sizes')
    clothes_colors = fields.Many2one(comodel_name='tenache89.clothes.colors')
    found = fields.Boolean(default=False)
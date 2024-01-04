 # -*- coding: utf-8 -*-
from odoo import models, fields, api, _, exceptions # _ is for translations
from odoo.exceptions import UserError
import datetime

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    clothes_types_id = fields.Many2one(comodel_name='tenache89.clothes.types')
    
   
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    new_field = fields.Char()
    clothes_type_id_template = fields.One2many(comodel_name='tenache89.clothes.types', inverse_name='clothes_product_id')
    clothes_type_id_string = fields.Char(related='clothes_type_id_template.tipo')
    
class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    clothes_type_id_product = fields.One2many(comodel_name='tenache89.clothes.types', inverse_name='product_id_type')
    
class ClothesType(models.Model):
    _name='tenache89.clothes.types'
    _description = "type of clothes (i.e. shirt, skirt, etc.)"
    _rec_name = "tipo"
    product_id_type = fields.Many2one(
        'product.product', string='Product', domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        change_default=True, ondelete='restrict', check_company=True)    
    tipo = fields.Char()
    clothes_product_id = fields.Many2one(comodel_name="product.template")
    clothes_product_id_id = fields.Integer(comodel_name="product.template", related="clothes_product_id.id")
    # clothes_product_id_id = fields.Integer(related="clothes_prouduct_id.id")
    product_id_name = fields.Char(related="clothes_product_id.name")

class ClothesItem(models.Model):
    _name ='tenache89.clothes.item'
    _description = 'Clothes Item'
    
    laundry_order_id = fields.Many2one(comodel_name='tenache89.sale.order')
    clothes_types = fields.Many2one(comodel_name='tenache89.clothes.types')
    clothes_colors = fields.Many2one(comodel_name='tenache89.clothes.colors')
    clothes_brands = fields.Many2one(comodel_name='tenache89.clothes.brands')
    clothes_sizes = fields.Many2one(comodel_name='tenache89.clothes.sizes')
    description = fields.Text()
    found = fields.Boolean(default=False)
    active = fields.Boolean(default=True)
    clothes_product_id = fields.Many2one(comodel_name='product.product')
    
    def clothes_found(self):
        if self.found:
            self.found = False
        else:
            self.found = True
            
class ClothesColor(models.Model):
    _name = 'tenache89.clothes.colors'
    _description = "clothes color"
    _rec_name = "color"
    
    color = fields.Char()
    
class ClothesBrand(models.Model):
    _name = 'tenache89.clothes.brands'
    _description = "clothes brand"
    _rec_name = "brand"
    
    brand = fields.Char()
    
class ClothesSize(models.Model):
    _name = 'tenache89.clothes.sizes'
    _description = "clothes size"
    _rec_name = "size"
    
    size = fields.Char()
    
class clothesPlace(models.Model):
    _name = 'tenache89.clothes.places'
    _description = "clothes place"
    _rec_name = "place"
        
    place = fields.Char()
    occupied = fields.Boolean()

## TODO: hay que hacer una funcion que haga obligatoria la descripcion del producto
## o al menos que salga un cartel pidiendo descripcion ... 
## TODO: hay que hacer un link entre el tipo de ropa y los productos. Asi cada tipo de ropa tiene un solo "producto" (ropa interior, etc.)

## TODO: hay que reincorporar esto de que aparezca el "a nombre de" cuando es consumidor final anonimo ... 
## Para eso hay que modificar el sale.order inherit


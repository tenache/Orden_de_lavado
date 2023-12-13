 # -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions # _ is for translations
from odoo.exceptions import UserError
import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    laundry_order_id = fields.Many2one(comodel_name='tenache89.sale.order')
    
class clothesCategory(models.Model):
    _name = 'tenache89.clothes.category'
    
    clothes_item_ids = fields.Many2one(comodel_name='tenache89.clothes.item')
    
    price = fields.Float()
    
class priceRule(models.Model):
    _name = 'tenache89.'
    
    

class SimilarItemWizard(models.TransientModel):
    _name = 'similar.item.wizard'
    _description = 'Similar Item Wizard'
    
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
    clothes_category_id = fields.One2many(comodel_name='tenache89.clothes.category', inverse_name='clothes_item_ids')
    
    def clothes_found(self):
        if self.found:
            self.found = False
        else:
            self.found = True
            
    # @api.onchange("clothes_types","clothes_colors","clothes_brands","clothes_sizes")
    # def find_similar_item(self):
    #     if self.clothes_types:
    #         items_env = self.env['tenache89.clothes.item']
    #         similar_items = items_env.search([
    #             ("clothes_types",'=',self.clothes_types.id),
    #             ("clothes_colors",'=',self.clothes_colors.id),
    #             ("clothes_brands",'=',self.clothes_brands.id),
    #             ("clothes_sizes",'=',self.clothes_sizes.id),
    #             ("found",'=',False),
    #         ])
    #         if not similar_items:                
    #             print("Different clothes type")
    #         else:
    #             raise exceptions.Warning("Cuidado: Hay Items con caracteristicas similares \n Por favor llene la descripcion")
    #             # TODO: intentar hacer la Descripcion obligatoria si es que encuentra una prenda igual ...
       
# class LaundryOrder(models.Model):
#     _inherit = "sale.order.line"
#     _name = 'tenache89.laundry.order'
#     _description = 'Laundry Order'

#     clothes_item_ids = fields.One2many(comodel_name='tenache89.clothes.item', inverse_name='laundry_order_id')
#     partner = fields.Many2one(comodel_name='res.partner')
#     partner_name = fields.Char(related="partner.name")
#     a_nombre = fields.Char()
#     delivered = fields.Boolean()
#     place_id = fields.Many2one(comodel_name="tenache89.clothes.places")
#     place_name = fields.Char(related="place_id.place")
#     place_occupied = fields.Boolean(related="place_id.occupied")
#     active = fields.Boolean(default=True)
    
        
#     @api.model
#     def create(self, vals):
#         similar_items = self.find_similar_item(vals)
#         if similar_items:
#             raise UserError(_("Hay otra prenda igual \n Tienes que agregar una descripcion"))
#         record_ = super(LaundryOrder, self).create(vals)
#         place = self.env["tenache89.clothes.places"].search([('id', '=', vals['place_id'])])
#         place.occupied = True

#         return record_
    
#     # @api.multi
#     def write(self, vals):
#         if 'active' in vals and not vals['active']:
#             for item in self.clothes_item_ids:
#                 item.write({'active':False})
#         similar_items = self.find_similar_item(vals)
        
#         if similar_items:
#             raise UserError(_("Hay otra prenda igual \n Tienes que agregar una descripcion"))
        
#         record = super(LaundryOrder, self).write(vals)
#         # search last = True. Cambialo por false
#         self.place_id.occupied = True
#         return record
    
#     def find_similar_item(self, vals):
#         all_similar_items = []
#         clothes_item_ids = []
#         if 'clothes_item_ids' in vals:
#             for item_id in vals['clothes_item_ids']:
#                 if type(item_id[2]) == dict:
#                     clothes_item_ids.append(item_id[2])
  
#         for clothes_item in clothes_item_ids:
#             if clothes_item['clothes_types']:
#                 items_env = self.env['tenache89.clothes.item']
#                 similar_items = items_env.search([
#                     ("clothes_types",'=',clothes_item['clothes_types']),
#                     ("clothes_colors",'=',clothes_item['clothes_colors']),
#                     ("clothes_brands",'=',clothes_item['clothes_brands']),
#                     ("clothes_sizes",'=',clothes_item['clothes_sizes']),
#                     ("description", '=', clothes_item['description']),
#                     ("found",'=',False),
#                 ])
#             if similar_items:
#                 all_similar_items.append(similar_items)
#         return all_similar_items
      
#     def deliver(self):
#         if self.delivered:
#             self.delivered = False
#             self.place_id.occupied = True
#         else:
#             self.delivered = True
#             self.place_id.occupied = False
#             for item in self.clothes_item_ids:
#                 item.found = False

class ClothesType(models.Model):
    _name='tenache89.clothes.types'
    _description = "type of clothes (i.e. shirt, skirt, etc.)"
    _rec_name = "tipo"
    
    tipo = fields.Char()
    
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

# drugs won't make up for the gap genetics create
# PED is rampant in female users... 
# 15 more minutes ... 

## TODO: Agregar funcion desde views_try para poner verdader-falso el ocupado o no ocupado ... 

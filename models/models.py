 # -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions # _ is for translations
from odoo.exceptions import UserError
import datetime

class SimilarItemWizard(models.TransientModel):
    _name = 'similar.item.wizard'
    _description = 'Similar Item Wizard'
    
class ClothesItem(models.Model):
    _name ='tenache89.clothes.item'
    _description = 'Clothes Item'
    
    laundry_order_id = fields.Many2one(comodel_name='tenache89.laundry.order')
    clothes_types = fields.Many2one(comodel_name='tenache89.clothes.types')
    clothes_colors = fields.Many2one(comodel_name='tenache89.clothes.colors')
    clothes_brands = fields.Many2one(comodel_name='tenache89.clothes.brands')
    clothes_sizes = fields.Many2one(comodel_name='tenache89.clothes.sizes')
    description = fields.Text()
    found = fields.Boolean(default=False)
    
    def clothes_found(self):
        if self.found:
            self.found = False
        else:
            self.found = True
            
    @api.onchange("clothes_types","clothes_colors","clothes_brands","clothes_sizes")
    def find_similar_item(self):
        if self.clothes_types:
            items_env = self.env['tenache89.clothes.item']
            similar_items = items_env.search([
                ("clothes_types",'=',self.clothes_types.id),
                ("clothes_colors",'=',self.clothes_colors.id),
                ("clothes_brands",'=',self.clothes_brands.id),
                ("clothes_sizes",'=',self.clothes_sizes.id),
                ("found",'=',False),
            ])
            if not similar_items:                
                print("Different clothes type")
            else:
                raise exceptions.Warning("Cuidado: Hay Items con caracteristicas similares \n Por favor llene la descripcion")
                # TODO:esto deberia printear un warning que diga: hay un item con las mismas caracteristicas.
                ## supongo que deberia ser un widget o algo asi? wizard? no se como se dice ...  
                # TODO: intentar hacer la Descripcion obligatoria si es que encuentra una prenda igual ...
       
class LaundryOrder(models.Model):
    _name = 'tenache89.laundry.order'
    _description = 'Laundry Order'

    clothes_item_ids = fields.One2many(comodel_name='tenache89.clothes.item', inverse_name='laundry_order_id')
    partner = fields.Many2one(comodel_name='res.partner')
    partner_name = fields.Char(related="partner.name")
    a_nombre = fields.Char()
    delivered = fields.Boolean()
    place_id = fields.Many2one(comodel_name="tenache89.clothes.places")
    place_name = fields.Char(related="place_id.place")
    place_occupied = fields.Boolean(related="place_id.occupied")
    
    @api.model
    def create(self, vals):
        record_ = super(LaundryOrder, self).create(vals)
        place = self.env["tenache89.clothes.places"].search([('id', '=', vals['place_id'])])
        place.occupied = True
        return record_
    
    def write(self, vals):
        record = super(LaundryOrder, self).write(vals)
        # search last = True. Cambialo por false
        self.place_id.occupied = True
        
        print("holaaaa")
        return record
      
    def deliver(self):
        if self.delivered:
            self.delivered = False
            self.place_id.occupied = True
        else:
            self.delivered = True
            self.place_id.occupied = False
            for item in self.clothes_item_ids:
                item.found = False

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

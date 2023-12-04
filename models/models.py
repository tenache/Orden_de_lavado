 # -*- coding: utf-8 -*-

from odoo import models, fields, api, _ # _ is for translations
from odoo.exceptions import UserError
import datetime


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
        # TODO: fijarse si esto esta bien o esta mal ... probarlo
            if not similar_items:
                print("Different clothes type")
            else:
                print("Same clothes type")
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
    
    def place_occupy(self):
        place_occupied = True 
    
    def place_vacate(self):
        place_occupied = False
        
    def deliver(self):
        if self.delivered:
            self.delivered = False
        # TODO: ver si esto funciona bien
        else:
            self.delivered = True
            for item in self.clothes_item_ids:
                item.found = True

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
    # hacer algun inverso sera necesario?? 
    
class clothesPlace(models.Model):
    _name = 'tenache89.clothes.places'
    _description = "clothes place"
    _rec_name = "place"
    
    place = fields.Char()
    occupied = fields.Boolean()
    
## TODO: search de todas las ordenes sin entregar y buscar si tienen todas las mismas caracteristicas (id).  
## TODO: esto ya esta hecho, basicamente. Hay que corroborar que todo funcione como se espera ... 
## TODO: Agregar en el general, la estanteria donde se tendria que guardar ... Hacerlo opcional, xq ya los conocemos ...
## TODO: poner nombre de cliente si tiene, y solo "a nombre" cuando no haya un cliente ... 
## que mas falta?? 
## TODO: hacer un github 
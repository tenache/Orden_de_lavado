from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrderLineLaundryInherit(models.Model):
    _inherit = 'sale.order.line'
    _description = 'This model adds characteristics of the clothes that make it easily recognizable'
    
    # algun dia para hacer mas simple la vista, sacar la columna impuestos tal como esta y poner una booleana, ya 
    # que casi siempre es IVA
    # taxes = fields.Boolean(default=False)
    clothes_item_ids = fields.One2many(comodel_name='tenache89.clothes.item', inverse_name='laundry_order_id')
    clothes_types = fields.Many2one(comodel_name='tenache89.clothes.types')
    clothes_brands = fields.Many2one(comodel_name='tenache89.clothes.brands')
    clothes_sizes = fields.Many2one(comodel_name='tenache89.clothes.sizes')
    clothes_colors = fields.Many2one(comodel_name='tenache89.clothes.colors')
    found = fields.Boolean(default=False)
    clothes_description = fields.Text()
    
    mandatory_description = fields.Boolean(default=True)
    


    @api.model
    def create(self, vals):
        similar_items = self.find_similar_item(vals)
        vals['mandatory_description'] = bool(similar_items)
        # if similar_items:
        #     raise UserError(_("Hay otra prenda igual \n Tienes que agregar una descripcion"))
        record_ = super(SaleOrderLineLaundryInherit, self).create(vals)
        # place = self.env["tenache89.clothes.places"].search([('id', '=', vals['place_id'])])
        # place.occupied = True

        return record_
    
    def write(self, vals):
        if 'active' in vals and not vals['active']:
            for item in self.clothes_item_ids:
                item.write({'active':False})
        similar_items = self.find_similar_item(vals)
        vals['mandatory_description'] = not bool(similar_items)
        
        # if similar_items:
        #     raise UserError(_("Hay otra prenda igual \n Tienes que agregar una descripcion"))
        
        record = super(SaleOrderLineLaundryInherit, self).write(vals)
        # search last = True. Cambialo por false
        # self.place_id.occupied = True
        return record
    
    def find_similar_item(self):
        all_similar_items = []
        domain_filter = []
        all_chars = [self.clothes_types.id, self.clothes_colors.id, self.clothes_sizes.id, self.clothes_description]
        # domain_filter = [
        #      '|','|', ('clothes_types', '=', self.clothes_types.id), ('clothes_types', '=', False),
        #      '|','|', ('clothes_colors', '=', self.clothes_colors.id), ('clothes_colors', '=', False),
        #      '|','|', ('clothes_brands', '=', self.clothes_brands.id), ('clothes_brands', '=', False),
        #      '|','|', ('clothes_sizes', '=', self.clothes_sizes.id), ('clothes_sizes', '=', False), 
        #      '|','|', ('description', '=', self.clothes_description), ('description', '=', False), 
        #     ('found', '=', False),
        #             ]
        
        items_env = self.env['tenache89.clothes.item']
        all_char_names = ['clothes_types','clothes_colors','clothes_brands','clothes_sizes','description']
        similar_items = []
        for i, char in enumerate(all_chars):
            if char:
                similar_item = items_env.search([
                    '|','|', (all_char_names[i], '=', char), (all_char_names[i], '=', False),
                    ('found', '=', False),
                ])
                print('domain')
                if similar_item:
                    similar_items.append(True)
                else:
                    similar_items.append(False)
            else:
                similar_items.append(True)
        if sum(similar_items) == 5:
            return True
        else:
            return False
                    
                    
        # if self.clothes_types:
        #     items_env = self.env['tenache89.clothes.item']
        #     similar_items = items_env.search(domain_filter)
        #     print('hello3')

        # if similar_items:
        #         all_similar_items.extend(similar_items)
        #         print('hello')
        # return all_similar_items
    
    @api.onchange('clothes_types', 'clothes_brands', 'clothes_sizes', 'clothes_colors')
    def _onchange_clothes_fields(self):
        if self.clothes_types.id:
            similar_items = self.find_similar_item()
            self.mandatory_description = bool(similar_items)  
            print('hello')
            print('hello2')
    
 

    
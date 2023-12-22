from odoo import models, fields, api, _

class SaleOrderLaundryInherit(models.Model):
    _inherit = 'sale.order'
    _description = 'DESC AQUI'
    
    place_id = fields.Many2one(comodel_name="tenache89.clothes.places")
    
    ironing = fields.Boolean(default=False)
    
    display_state = fields.Selection([
        ('Por lavar','Por lavar'),
        ('Por planchar','Por planchar'),
        ('Por retirar','Por retirar'),
        ('Retirado','Retirado'),
        ], string="Estado", default='Por lavar')

    
    def change_state(self):
        if self.display_state == 'Por lavar':
            if self.ironing:
                self.display_state = 'Por planchar'
            else:
                self.display_state = 'Por retirar'
        elif self.display_state == 'Por planchar':
            self.display_state = 'Por retirar'
        else:
            self.display_state = 'Retirado'
            
    def reverse_state(self):
        if self.display_state == 'Retirado':
            self.display_state = 'Por retirar'
        elif self.display_state == 'Por retirar':
            if self.ironing:
                self.display_state = 'Por planchar'
            else:
                self.display_state = 'Por lavar'
        else:
            self.display_state = 'Por lavar'
        


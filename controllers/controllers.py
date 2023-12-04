# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json 

class LocuraController(http.Controller): # va a actuar de controlador 
    @http.route('/api/locurajuvenil', auth='public', method=['GET'], csrf=False)
    def get_locura(self, **kwargs):
            try:
                locuras = http.request.env['tenache89.locurajuvenil'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
                res = json.dumps(locuras, ensure_ascii=False).encode('utf-8')
                return Response(res, content_type='application/json;charset=utf-8', status=200)
            except Exception as e:
                return Response(json.dumps({'error':str(e)}), content_type='application/json;charset=utf-8', status=505)

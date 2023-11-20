# -*- coding: utf-8 -*-
# from odoo import http


# class CustomOrders(http.Controller):
#     @http.route('/custom_orders/custom_orders', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_orders/custom_orders/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_orders.listing', {
#             'root': '/custom_orders/custom_orders',
#             'objects': http.request.env['custom_orders.custom_orders'].search([]),
#         })

#     @http.route('/custom_orders/custom_orders/objects/<model("custom_orders.custom_orders"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_orders.object', {
#             'object': obj
#         })

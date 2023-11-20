# -*- coding: utf-8 -*-
# from odoo import http


# class Orders(http.Controller):
#     @http.route('/orders/orders', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/orders/orders/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('orders.listing', {
#             'root': '/orders/orders',
#             'objects': http.request.env['orders.orders'].search([]),
#         })

#     @http.route('/orders/orders/objects/<model("orders.orders"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('orders.object', {
#             'object': obj
#         })

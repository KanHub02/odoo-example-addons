# -*- coding: utf-8 -*-
# from odoo import http


# class NmCustomers(http.Controller):
#     @http.route('/nm_customers/nm_customers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nm_customers/nm_customers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nm_customers.listing', {
#             'root': '/nm_customers/nm_customers',
#             'objects': http.request.env['nm_customers.nm_customers'].search([]),
#         })

#     @http.route('/nm_customers/nm_customers/objects/<model("nm_customers.nm_customers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nm_customers.object', {
#             'object': obj
#         })

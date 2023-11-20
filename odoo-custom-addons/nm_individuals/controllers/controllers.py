# -*- coding: utf-8 -*-
# from odoo import http


# class NmIndividuals(http.Controller):
#     @http.route('/nm_individuals/nm_individuals', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nm_individuals/nm_individuals/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nm_individuals.listing', {
#             'root': '/nm_individuals/nm_individuals',
#             'objects': http.request.env['nm_individuals.nm_individuals'].search([]),
#         })

#     @http.route('/nm_individuals/nm_individuals/objects/<model("nm_individuals.nm_individuals"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nm_individuals.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class NmLegalEntities(http.Controller):
#     @http.route('/nm_legal_entities/nm_legal_entities', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nm_legal_entities/nm_legal_entities/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nm_legal_entities.listing', {
#             'root': '/nm_legal_entities/nm_legal_entities',
#             'objects': http.request.env['nm_legal_entities.nm_legal_entities'].search([]),
#         })

#     @http.route('/nm_legal_entities/nm_legal_entities/objects/<model("nm_legal_entities.nm_legal_entities"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nm_legal_entities.object', {
#             'object': obj
#         })

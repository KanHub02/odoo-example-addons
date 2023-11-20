# -*- coding: utf-8 -*-
# from odoo import http


# class NmLeads(http.Controller):
#     @http.route('/nm_leads/nm_leads', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nm_leads/nm_leads/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nm_leads.listing', {
#             'root': '/nm_leads/nm_leads',
#             'objects': http.request.env['nm_leads.nm_leads'].search([]),
#         })

#     @http.route('/nm_leads/nm_leads/objects/<model("nm_leads.nm_leads"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nm_leads.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nm_individuals(models.Model):
#     _name = 'nm_individuals.nm_individuals'
#     _description = 'nm_individuals.nm_individuals'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

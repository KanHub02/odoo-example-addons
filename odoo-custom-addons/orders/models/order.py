from odoo import models, fields
from odoo import  _

class CustomOrder(models.Model):
    _name = 'custom.order'
    _description = 'Custom Order'

    name = fields.Char(_('Order Reference'), required=True)
    date_order = fields.Datetime('Order Date', required=True, index=True, copy=False, default=fields.Datetime.now)
    order_line_ids = fields.One2many('custom.order.line', 'order_id', string='Order Lines')

class CustomOrderLine(models.Model):
    _name = 'custom.order.line'
    _description = 'Custom Order Line'

    order_id = fields.Many2one('custom.order', string='Order Reference', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_qty = fields.Float(string='Quantity', default=1.0)

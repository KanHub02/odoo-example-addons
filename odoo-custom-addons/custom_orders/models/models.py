# models.py
from odoo import models, fields, api


class Order(models.Model):
    _name = 'custom.order'
    _description = 'Custom Order'

    invoice_no = fields.Char('№ Инвойса ', required=True)
    invoice_prefix = fields.Selection([('Коммерческий', 'Коммерческий '), ('Проформа-инвойс', 'Проформа-инвойс')], string='Префикс инвойса')
    payment_due_date = fields.Date('Срок оплаты')
    invoice_date = fields.Date('Дата инвойса')
    currency_id = fields.Many2one('res.currency', 'Курс валют')
    responsible_operation_id = fields.Many2one('res.users', 'Ответственный')
    responsible_sales_id = fields.Many2one('res.users', 'Ответственный за продажу')
    customer_type = fields.Selection([('Физическое', 'Физическое'), ('Юридическое', 'Юридическое')], string='Физическое/Юридическое лицо')

    def button_create_order_in_1C(self):
        pass

    def button_create_payment_record(self):
        pass

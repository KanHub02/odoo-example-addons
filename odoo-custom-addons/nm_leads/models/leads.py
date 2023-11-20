from odoo import  models, fields
import time


class Lead(models.Model):
    _name = "nm_leads.lead"

    last_name = fields.Char(string="Фамилия")
    name = fields.Char(string="Имя")
    middle_name = fields.Char(string="Отчество")
    phone_number = fields.Char(string="Номер телефона")
    reference_source = fields.Selection([
        ("Источник 1", "Источник 1"),
        ("Источник 2", "Источник 2"),
        ("Источник 3", "Источник 3"),
    ], string="Источник обращения")
    mail = fields.Char(string="Почта")
    status = fields.Selection([
        ("В ожидании", "В ожидании"),
        ("Просмотрен", "Просмотрен")
    ])
    request_goal = fields.Char(string="Цель обращения")
    create_from = fields.Many2one("res.users", string="Кем создано")
    created_at = fields.Datetime("Дата создания", required=False, readonly=False, select=True)
    comment = fields.Char("Коментарии")


    _defaults = {
        'created_at': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
    }

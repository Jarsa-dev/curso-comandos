# -*- coding: utf-8 -*-
# Copyright 2018, Jarsa Sistemas
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many(
        'openacademy.session',
        string="Attended Sessions",
        readonly=True)

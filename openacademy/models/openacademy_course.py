# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one(
        'res.users',
        ondelete='set null',
        string="Responsible",
        index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

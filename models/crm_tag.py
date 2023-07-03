# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class CrmTag(models.Model):
    _name = 'crm.tag'
    _description = 'Tag'

    name = fields.Char(string='Name', required=True)
    id = fields.Integer(string='ID')
    color = fields.Integer(string='Color', required=True)

    sequence = fields.Integer(string='Secuencia', default=10)

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]
# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('crm.tag', string='Tags')

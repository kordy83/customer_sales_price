# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SalesPrice(models.Model):
    _inherit = ['product.template']
    
    customer_sales_price = fields.Float('سعر البيع للمستهلك', default=1.0, help="Price at which the product is sold to end customers.")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_cp = fields.Float('customer price', related='product_id.customer_sales_price', store=True)
    
class AccountMove(models.Model):
    _inherit = 'account.move.line'

    product_cpa = fields.Float('customer price', related='product_id.customer_sales_price', store=True)
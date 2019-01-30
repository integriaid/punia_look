from __future__ import unicode_literals

import frappe
import frappe.defaults

def update_website_context(context):
     context.update(dict(
         brand_html='<img src="/assets/punialook/img/brand-logo.png" >',
        #  hide_login=True,
        #  footer="Disediakan oleh Punia Online"
     ))
     return context

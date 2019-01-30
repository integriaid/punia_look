# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "punia_look"
app_title = "Punia Look"
app_publisher = "Punia Dev"
app_description = "punia corp look"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dev@punia.online"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/punia_look.min.css"
app_include_js = [
	"/assets/punia_look/js/punia_look.js"
	# "/assets/punia_look/js/modules.js"
]

# include js, css files in header of web template
web_include_css = "/assets/css/punia_look-web.min.css"
web_include_js = "/assets/punia_look/js/punia_look.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "punia_look.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "punia_look.install.before_install"
# after_install = "punia_look.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "punia_look.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"punia_look.tasks.all"
# 	],
# 	"daily": [
# 		"punia_look.tasks.daily"
# 	],
# 	"hourly": [
# 		"punia_look.tasks.hourly"
# 	],
# 	"weekly": [
# 		"punia_look.tasks.weekly"
# 	]
# 	"monthly": [
# 		"punia_look.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "punia_look.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "punia_look.event.get_events"
# }

# punia images
website_context = {
	"favicon": "/assets/punia_look/img/favicon.ico",
	"email_brand_image": "assets/punia_look/img/punia-logo.png",
	"splash_image": "assets/punia_look/img/online-store.png",
	# "company_logo": "assets/punia_look/img/p-logo.png"
}

update_website_context = "punia_look.punia_look.website_context.update_website_context"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://punia.online?source=via_email_footer" target="_blank">
			Punia Online
		</a>
	</span>
"""

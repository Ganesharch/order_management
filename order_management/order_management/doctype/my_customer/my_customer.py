# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nishta Solutions and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MyCustomer(Document):
	pass


@frappe.whitelist()
def get_city(doctype, txt, searchfield, start, page_len, filters):
	state = filters.get('state')
	if not state:
		return []
	print frappe.db.sql("select name from tabCity where state='{state}'".format(state=state))
	return frappe.db.sql("select name from tabCity where state=%s and name like %s", (state, txt + "%"))



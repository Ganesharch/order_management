frappe.ui.form.on("My Customer", "state", function(frm) {
	cur_frm.set_query("city", function() {
		return {
			query: "order_management.order_management.doctype.my_customer.my_customer.get_city",
			filters: {
				state: frm.doc.state
			}
		}
	})
});

frappe.provide('erpnext');

// add toolbar icon
$(document).bind('toolbar_setup', function () {
    // frappe.app.name = "ERPNext";

    frappe.help_feedback_link = '<p><a class="text-muted" \
		href="https://masukan.punia.online">Feedback</a></p>'


    $('.navbar-home').html('<img class="erpnext-icon" src="' +
        frappe.urllib.get_base_url() + '/assets/punia_look/img/home_icon.png" />');

    // $('[data-link="docs"]').attr("href", "https://docs.punia.online")
    // $('[data-link="issues"]').attr("href", "https://github.com/frappe/erpnext/issues")


    // default documentation
    $('[data-link-type="documentation"]').attr('data-path', 'http://docs.punia.online/');
    $('[data-link-type="forum"]').attr('data-path', 'http://forum.punia.online/');

    // additional help links for erpnext
    var $help_menu = $('.dropdown-help ul .documentation-links');

    // $('<li><a data-link-type="forum" href="https://diskusi.punia.online" \
		// target="_blank">' + __('Forum Pengguna') + '</a></li>').insertBefore($help_menu);
    // $('<li class="gitter-chat-link"><a href="https://chat.punia.online" \
		// target="_blank">' + __('WA Group') + '</a></li>').insertBefore($help_menu);
    // $('<li><a href="https://www.punia.online/contact" \
		// target="_blank">' + __('Kirim Masukan') + '</a></li>').insertBefore($help_menu);

});

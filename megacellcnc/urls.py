from django.urls import path
from megacellcnc import megacellcnc_views
from django.shortcuts import get_object_or_404, redirect
from megacellcnc.models import Project  # Ensure this import is correct

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('megacellcnc:project')

app_name = 'megacellcnc'
urlpatterns = [
    path('', megacellcnc_views.index, name="index"),
    path('index/', megacellcnc_views.index, name="index"),
    path('settings/', megacellcnc_views.settings, name="settings"),
    path('project/', megacellcnc_views.project, name="project"),
    path('project-details/', megacellcnc_views.project_details, name="project-details"),
    path('projectdetails/<int:project_id>/update-slots/', megacellcnc_views.get_project_slots, name='project-update-slots'),
    path('new-project/', megacellcnc_views.new_project, name="new-project"),
    path('devices/', megacellcnc_views.devices, name="devices"),
    path('database/', megacellcnc_views.database, name="database"),
    path('batteries/', megacellcnc_views.batteries, name="batteries"),
    path('add-battery/', megacellcnc_views.add_battery, name="add-battery"),
    path('save-battery-configuration/', megacellcnc_views.save_battery_configuration, name="save-battery-configuration"),
    path('add-cell/', megacellcnc_views.add_cell, name="add-cell"),
    path('get-cells/', megacellcnc_views.get_cells, name="get-cells"),
    path('get-battery-cells/', megacellcnc_views.get_battery_cells, name="get-battery-cells"),
    path('delete-cells/', megacellcnc_views.delete_cells, name="delete-cells"),
    path('device-slots/', megacellcnc_views.device_slots, name="device-slots"),
    path('device/<int:device_id>/update-slots/', megacellcnc_views.get_updated_slots, name='update-slots'),
    path('slot/action/', megacellcnc_views.handle_device_action, name='action'),
    path('delete-devices/', megacellcnc_views.delete_devices, name='delete-devices'),
    path('new-device/', megacellcnc_views.new_device, name="new-device"),
    path('edit-device/', megacellcnc_views.edit_device, name='edit-device'),
    # Add the delete-project path
    path('delete-project/<int:project_id>/', delete_project, name='delete-project'),
    path('save-device-settings/', megacellcnc_views.save_device_settings, name='save-device-settings'),
    path('save-printer-settings/', megacellcnc_views.save_printer_settings, name='save-printer-settings'),
    path('get-printer-settings/', megacellcnc_views.get_printer_settings, name='get-printer-settings'),
    path('print-label/', megacellcnc_views.print_label, name='print-label'),

    path('save-cell/', megacellcnc_views.save_cell, name='save-cell'),
    path('get-history/', megacellcnc_views.get_history, name='get-history'),
    path('scan-devices/', megacellcnc_views.scan_devices, name='scan-devices'),

    # path('employee/',megacellcnc_views.employee,name="employee"),
    path('core-hr/', megacellcnc_views.core_hr, name="core-hr"),
    path('finance/', megacellcnc_views.finance, name="finance"),
    path('task/', megacellcnc_views.task, name="task"),
    path('task-summary/', megacellcnc_views.task_summary, name="task-summary"),
    path('performance/', megacellcnc_views.performance, name="performance"),

    path('reports/', megacellcnc_views.reports, name="reports"),
    path('manage-clients/', megacellcnc_views.manage_clients, name="manage-clients"),
    path('blog-1/', megacellcnc_views.blog_1, name="blog-1"),
    path('svg-icon/', megacellcnc_views.svg_icon, name="svg-icon"),

    path('auto-write/', megacellcnc_views.auto_write, name="auto-write"),
    path('chatbot/', megacellcnc_views.chatbot, name="chatbot"),
    path('fine-tune-models/', megacellcnc_views.fine_tune_models, name="fine-tune-models"),
    path('imports/', megacellcnc_views.imports, name="imports"),
    path('prompt/', megacellcnc_views.prompt, name="prompt"),
    path('repurpose/', megacellcnc_views.repurpose, name="repurpose"),
    path('rss/', megacellcnc_views.rss, name="rss"),
    path('scheduled/', megacellcnc_views.scheduled, name="scheduled"),
    path('setting/', megacellcnc_views.setting, name="setting"),

    path('content/', megacellcnc_views.content, name="content"),
    path('add-content/', megacellcnc_views.add_content, name="add-content"),
    path('menu/', megacellcnc_views.menu, name="menu"),
    path('email-template/', megacellcnc_views.email_template, name="email-template"),
    path('add-email/', megacellcnc_views.add_email, name="add-email"),
    path('blog/', megacellcnc_views.blog, name="blog"),
    path('add-blog/', megacellcnc_views.add_blog, name="add-blog"),
    path('blog-category/', megacellcnc_views.blog_category, name="blog-category"),

    path('chat/', megacellcnc_views.chat, name="chat"),
    path('user/', megacellcnc_views.user, name="user"),
    path('user-roles/', megacellcnc_views.user_roles, name="user-roles"),
    path('app-profile-1/', megacellcnc_views.app_profile_1, name="app-profile-1"),
    path('app-profile-2/', megacellcnc_views.app_profile_2, name="app-profile-2"),
    path('edit-profile/', megacellcnc_views.edit_profile, name="edit-profile"),
    path('post-details/', megacellcnc_views.post_details, name="post-details"),
    path('customer/', megacellcnc_views.customer, name="customer"),
    path('customer-profile/', megacellcnc_views.customer_profile, name="customer-profile"),
    path('contacts/', megacellcnc_views.contacts, name="contacts"),
    path('email-compose/', megacellcnc_views.email_compose, name="email-compose"),
    path('email-inbox/', megacellcnc_views.email_inbox, name="email-inbox"),
    path('email-read/', megacellcnc_views.email_read, name="email-read"),
    path('app-calender/', megacellcnc_views.app_calender, name="app-calender"),
    path('ecom-product-grid/', megacellcnc_views.ecom_product_grid, name="ecom-product-grid"),
    path('ecom-product-list/', megacellcnc_views.ecom_product_list, name="ecom-product-list"),
    path('ecom-product-detail/', megacellcnc_views.ecom_product_detail, name="ecom-product-detail"),
    path('ecom-product-order/', megacellcnc_views.ecom_product_order, name="ecom-product-order"),
    path('ecom-checkout/', megacellcnc_views.ecom_checkout, name="ecom-checkout"),
    path('ecom-invoice/', megacellcnc_views.ecom_invoice, name="ecom-invoice"),
    path('ecom-customers/', megacellcnc_views.ecom_customers, name="ecom-customers"),
    path('chart-flot/', megacellcnc_views.chart_flot, name="chart-flot"),
    path('chart-morris/', megacellcnc_views.chart_morris, name="chart-morris"),
    path('chart-chartjs/', megacellcnc_views.chart_chartjs, name="chart-chartjs"),
    path('chart-chartist/', megacellcnc_views.chart_chartist, name="chart-chartist"),
    path('chart-sparkline/', megacellcnc_views.chart_sparkline, name="chart-sparkline"),
    path('chart-peity/', megacellcnc_views.chart_peity, name="chart-peity"),

    path('ui-accordion/', megacellcnc_views.ui_accordion, name="ui-accordion"),
    path('ui-alert/', megacellcnc_views.ui_alert, name="ui-alert"),
    path('ui-badge/', megacellcnc_views.ui_badge, name="ui-badge"),
    path('ui-button/', megacellcnc_views.ui_button, name="ui-button"),
    path('ui-modal/', megacellcnc_views.ui_modal, name="ui-modal"),
    path('ui-button-group/', megacellcnc_views.ui_button_group, name="ui-button-group"),
    path('ui-list-group/', megacellcnc_views.ui_list_group, name="ui-list-group"),
    path('ui-media-object/', megacellcnc_views.ui_media_object, name="ui-media-object"),
    path('ui-card/', megacellcnc_views.ui_card, name="ui-card"),
    path('ui-carousel/', megacellcnc_views.ui_carousel, name="ui-carousel"),
    path('ui-dropdown/', megacellcnc_views.ui_dropdown, name="ui-dropdown"),
    path('ui-popover/', megacellcnc_views.ui_popover, name="ui-popover"),
    path('ui-progressbar/', megacellcnc_views.ui_progressbar, name="ui-progressbar"),
    path('ui-tab/', megacellcnc_views.ui_tab, name="ui-tab"),
    path('ui-typography/', megacellcnc_views.ui_typography, name="ui-typography"),
    path('ui-pagination/', megacellcnc_views.ui_pagination, name="ui-pagination"),
    path('ui-grid/', megacellcnc_views.ui_grid, name="ui-grid"),

    path('uc-select2/', megacellcnc_views.uc_select2, name="uc-select2"),
    path('uc-nestable/', megacellcnc_views.uc_nestable, name="uc-nestable"),
    path('uc-noui-slider/', megacellcnc_views.uc_noui_slider, name="uc-noui-slider"),
    path('uc-sweetalert/', megacellcnc_views.uc_sweetalert, name="uc-sweetalert"),
    path('uc-toastr/', megacellcnc_views.uc_toastr, name="uc-toastr"),
    path('map-jqvmap/', megacellcnc_views.map_jqvmap, name="map-jqvmap"),
    path('uc-lightgallery/', megacellcnc_views.uc_lightgallery, name="uc-lightgallery"),

    path('widget-basic/', megacellcnc_views.widget_basic, name="widget-basic"),

    path('form-element/', megacellcnc_views.form_element, name="form-element"),
    path('form-wizard/', megacellcnc_views.form_wizard, name="form-wizard"),
    path('form-editor/', megacellcnc_views.form_editor, name="form-editor"),
    path('form-pickers/', megacellcnc_views.form_pickers, name="form-pickers"),

    path('table-bootstrap-basic/', megacellcnc_views.table_bootstrap_basic, name="table-bootstrap-basic"),
    path('table-datatable-basic/', megacellcnc_views.table_datatable_basic, name="table-datatable-basic"),

    path('page-login/', megacellcnc_views.page_login, name="page-login"),
    path('page-register/', megacellcnc_views.page_register, name="page-register"),
    path('page-forgot-password/', megacellcnc_views.page_forgot_password, name="page-forgot-password"),
    path('page-lock-screen/', megacellcnc_views.page_lock_screen, name="page-lock-screen"),
    path('page-empty/', megacellcnc_views.page_empty, name="page-empty"),
    path('page-error-400/', megacellcnc_views.page_error_400, name="page-error-400"),
    path('page-error-403/', megacellcnc_views.page_error_403, name="page-error-403"),
    path('page-error-404/', megacellcnc_views.page_error_404, name="page-error-404"),
    path('page-error-500/', megacellcnc_views.page_error_500, name="page-error-500"),
    path('page-error-503/', megacellcnc_views.page_error_503, name="page-error-503"),
]

function init() {
    $.djangocsrf("enable");
}

function on_list_loaded(data) {
    document.write(data)
}

function load_grocery_list() {
    $.ajax("/api/list", on_list_loaded)
}


function create_list_item(list_item) {
    $('#list').append("<div class='line'>" +
    "   <div class='check'><input type='checkbox' value='" + list_item.done + " onclick='check_click(" + list_item.id + ")'></div>" +
    "   <div class='name'>" + list_item.title + "</div>" +
        //"   <div class='due'>" + list_item.due + "</div>" +
    "</div>")
}

function add_new_item() {
    $('#add_btn').attr('disabled', 'disabled');
    $('#add').show();
}

function save_new_item() {
    var csrftoken = $.cookie('csrftoken');

    var list_item_title = $('#new_list_item').val();

    var list_item = [{'title': list_item_title, 'due': new Date().toJSON()}];

    $('#new_list_add').attr('disabled', 'disabled');
    $.ajax({
        url: '/api/add',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(list_item),
        processData: false,
        success: on_successful_save
    })
}

function on_successful_save() {
    $('#new_list_add').removeAttr('disabled');
    $('#add_btn').removeAttr('disabled');
    $('#add').hide();
}
function init() {
    $.djangocsrf("enable"); // does not work for some reason

    $('#new_list_item').keyup(update_suggestions)
}

function update_suggestions() {
    var text = $('#new_list_item').val();
    $.ajax({
        url: 'api/suggest',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'text': text}),
        processData: false,
        success: on_receive_suggestions
    })
}

function on_receive_suggestions(data) {
    $('#new_list_item').autocomplete({source: data});
}

function on_list_loaded(data) {
    if (data.length == 0) {
        $("#empty").show();
    } else {
        $("#empty").hide();
    }
    $("#list").html("");
    data.forEach(function (item) {
        create_list_item(item);
    })
}

function load_grocery_list() {
    $.ajax(
        {
            url: "/api/list",
            success: on_list_loaded
        });
}

function create_list_item(list_item) {
    $('#list').append("<div class='line-" + list_item.id + "'>" +
    "   <div class='check'><input type='checkbox' value='" + list_item.done + " onclick='check_click(" + list_item.id + ")'></div>" +
    "   <div class='name'>" + list_item.title + "</div>" +
        //"   <div class='due'>" + list_item.due + "</div>" +
    "<div id='delete-" + list_item.id + "' class='button2'>" +
    "<img src='/static/img/delete.png' width ='25' height='28' onclick='delete_item(" + list_item.id + ")' title='Delete'>" +
    "</div>" +
    "</div>");

    $('#line-' + list_item.id).hover(function () {
            $('#delete-' + list_item.id).show();
        },
        function () {
            $('#delete-' + list_item.id).hide();
        })
}

function delete_item(id) {
    $.ajax({
        url: 'api/delete',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'id': id}),
        processData: false,
        success: function () {
            load_grocery_list();
        }
    })
}

function cancel_new_item() {
    $('#add').hide();
    $('#add_btn').removeAttr('disabled');
    $('#new_list_item').val('');
}

function add_new_item() {
    $('#add_btn').attr('disabled', 'disabled');
    $('#add').show();
    $('#new_list_item').focus()
}

function save_new_item() {
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
    $('#new_list_item').val('');
    load_grocery_list();
}
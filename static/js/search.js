var getParameterByName = function(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var showUserSelected = function(selector) {
    var selection = getParameterByName(selector);
    if (selection) {
        $("." + selector + " input[value=\"" + selection + "\"]").prop("checked", true);
    }
}

var showLoading = function() {
    $("#loading").hide();
    $("#update_button").click(function(event) {
        $("#loading").show();
        $("#results").hide();
    });
}

$(document).ready(function() {
    showLoading();
    showUserSelected("term");
    showUserSelected("scope");
});

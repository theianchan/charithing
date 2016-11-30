var getParameterByName = function(name, url) {
    console.log("3");
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var showUserSelected = function(selector) {
    console.log("2");
    var selection = getParameterByName(selector);
    console.log("4");
    if (selection) {
        console.log("5");
        $("." + selector + " input[value=" + selection + "]").prop("checked", true);
        console.log("6");
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
    console.log("1");
    showUserSelected("cause");
    showUserSelected("scope");
});

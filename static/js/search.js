var showLoading = function() {
    $("#update_button").click(function(event) {
        $("#loading").show();
        $("#results").hide();
    });
}

$(document).ready(function() {
    $("#loading").hide();
    showLoading();
});

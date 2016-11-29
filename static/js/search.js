
// $("#update_button").click(function() {

//     var checkedCategories = $(".causes [type=checkbox]:checked");
//     var categoryIds = [];
//     for (var x = 0; x < checkedCategories.length; x++) {
//         categoryIds.push($(checkedCategories[x]).data("cause-id"));
//     }

//     var settings = {
//       "async": true,
//       "crossDomain": true,
//       "url": "http://api.charitynavigator.org/api/v1/causes/?causes=[" + categoryIds + "]&app_key=73973e687b179c033a5a40981816be38&app_id=1b9235b1",
//       "method": "GET",
//       "headers": {
//         "cache-control": "no-cache",
//         "postman-token": "7dcbf10f-954d-9071-594f-5e765ca872e7"
//       }
//     }

//     $.ajax(settings).done(function (response) {
//       console.log(response);
//     });
// });

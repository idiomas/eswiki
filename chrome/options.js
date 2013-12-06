// Restores articulos to saved values from localStorage.
function restore_saved() {
  var select = document.getElementById("articulos");
  chrome.storage.local.get(null, function(items) {
    select.innerHTML += "<br>" + "[";
    for (item in items) {
      select.innerHTML += "<br>" + "\"" + items[item] + "\"" + ",";
    }
    select.innerHTML += "<br>" + "]";
  });
}

//Clears all saved links from local storage
function clearall() {
  chrome.storage.local.clear(); 
}

//Load saved wiki articles on contenLoaded
document.addEventListener('DOMContentLoaded', restore_saved);

//clear all saved when button clicked
document.querySelector('#clear').addEventListener('click', clearall);

//function set_display() {
//  var set = null;
//  document.getElementById("display").href = set;
//}

//set filepath to append *.html filelinkon button click
//document.querySelector('#setdisplay').addEventListener('click', setdisplay);

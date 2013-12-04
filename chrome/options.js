//Loads favorites from LocalStorage
function load_saved() {
    chrome.storage.local.get(null, function (items){
        console.log(items);
    });
    //console.log(lst);
    lst = "fuckas";
    var status2 = document.getElementById("status2");
    status2.innerHTML = lst;
};



// Saves options to localStorage
function save_options() {
  var select = document.getElementById("color");
  var color = select.children[select.selectedIndex].value;
  localStorage["favorite_color"] = color;

  // Update status to let user know options were saved.
}

// Restores select box state to saved value from localStorage.
function restore_options() {
  var favorite = localStorage["favorite_color"];
  if (!favorite) {
    return;
  }
  var select = document.getElementById("color");
  for (var i = 0; i < select.children.length; i++) {
    var child = select.children[i];
    if (child.value == favorite) {
      child.selected = "true";
      break;
    }
  }
}
//document.addEventListener('DOMContentLoaded', restore_options);
document.querySelector('#load').addEventListener('click', load_saved);

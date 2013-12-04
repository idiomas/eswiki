function save_options() {
  var url = global;
  var status = document.getElementById("status");
  status.innerHTML = "Preference Saved.";
  // Check that there's some code there.
  if (!theValue) {
    message('Error: No value specified');
    return;
  }
  chrome.storage.local.set(url, function() {
    // Notify that we saved.
  });
}

console.log(global);
document.querySelector('#save').addEventListener('click', save_options);

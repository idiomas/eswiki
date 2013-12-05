var interwiki = null;

if (typeof document.getElementsByClassName('interwiki-es')[0] != "undefined") {
 interwiki = document.getElementsByClassName('interwiki-es')[0].innerHTML;
}

var regex = new RegExp('es\.wikipedia\.org/wiki/[^\s"]+\"');
var match = regex.exec(interwiki);
console.log(match);

if (match != null) {
  var url = "http://" + match;
  chrome.runtime.sendMessage(url);
}

//function checkForCorrelate(tabId, changeInfo, tab) {
//    if () {
//        return true;
//    }
//    return false;
//};
var gurl;
var savedKey;

function checkExistence(url){
  setUrl(url);
  chrome.storage.local.get(null, function(saved) {
    for (var key in saved) {
      console.log(key + " : " + saved[key]);
      if (gurl == saved[key]) {
        savedKey = key;
        isSaved(true);
        return;
      }   
    }
    console.log("isNotSaved");
    isSaved(false);
  });
}

function setUrl(url) {
  gurl = url;
  return;
}

function isSaved(bool) {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var tabId = tabs[0].id;
    if (bool) {
      chrome.pageAction.show(tabId);
      chrome.pageAction.setIcon({tabId: tabId, path: 'icon.png'});
      chrome.pageAction.onClicked.addListener(remove_url);
      console.log('ready to remove');
      return;
    }
    else {
      chrome.pageAction.show(tabId);
      chrome.pageAction.setIcon({tabId: tabId, path: 'icon2.png'});
      chrome.pageAction.onClicked.addListener(save_url);
      console.log('ready to save');
      return;
    }
  });
}

chrome.runtime.onMessage.addListener(checkExistence);

function save_url(tab) {
  chrome.pageAction.onClicked.removeListener(save_url);
  var time = new Date().toJSON().toString(); 
  var item = {};
  item[time] = gurl;
  console.log("i am being saved: " + gurl);
  chrome.storage.local.set(item);
  chrome.pageAction.setIcon({tabId: tab.id, path: 'icon.png'});
  return;
}

function remove_url(tab) {
  chrome.pageAction.onClicked.removeListener(remove_url);
  console.log("i am being removed: " + savedKey);
  chrome.storage.local.remove(savedKey);
  chrome.pageAction.setIcon({tabId: tab.id, path: 'icon2.png'});
  return;
}

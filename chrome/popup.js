var global = "Foo"
;(function(){
    var url;
    chrome.tabs.query({'active': true}, function (tabs) {
        url = tabs[0].url;
        console.log(url);
        if (wikidict[url]) {
            console.log(wikidict[url]);
            global  = {url: wikidict[url]}; 
            chrome.browserAction.setIcon({path: 'icon.png'});
        }
        else {
            console.log('does not return');
            chrome.browserAction.setIcon({path: 'icon2.png'});
            return false;
        }
        console.log(global);
    });
})();
    

 

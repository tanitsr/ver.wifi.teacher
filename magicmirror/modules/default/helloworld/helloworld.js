/* global Module */

/* Magic Mirror
 * Module: HelloWorld
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 */
//var weight = 0;
//let fs = require('fs');
//var get = require('./getpayload.js')
Module.register("helloworld",{
	
	// Default module config.
	defaults: {
		updateInterval: 500
	},

	start: function(){
		this.sendSocketNotification("START", this.config);
	},

	socketNotificationReceived: function(notification, payload) {
		if(notification === "DATA"){
			this.dataFile = payload;
			this.updateDom();
		}
	},

	
	getDom: function() {
		//weight = 50;	
		var wrapper = document.createElement("div");
		if(this.dataFile){
			var payload = this.dataFile.split("\n").join('');
			wrapper.innerHTML = payload;				
		}else{
			wrapper.innerHTML = "Please Input Phonenumber....";
			wrapper.className = "small"
		}
		return wrapper;
	}

	
});

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
		updateInterval: 3 * 1000
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
			var payload = this.dataFile.split("\n");
			wrapper.innerHTML = payload[0] + "<br>" 
			+ payload[1] + "<br>" + payload[2] + "<br>" +
			payload[3] + "<br>" + payload[4] + "<br>" + 
			payload[5] + "<br>" + payload[6] + "<br>" +
			payload[7] + "<br>" + payload[8] + "<br>" + 
			payload[9] + "<br>" + payload[10];						
		}else{
			wrapper.innerHTML = "No DATA!";
		}
		return wrapper;
	}

	
});

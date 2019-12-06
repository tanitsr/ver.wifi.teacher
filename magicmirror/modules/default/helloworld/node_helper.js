const NodeHelper = require("node_helper");
const fs = require("fs");

module.exports = NodeHelper.create({
//here comes the part of the nodehelper after the 3 dots as posted above

	socketNotificationReceived: function(notification, payload) {
		if(notification === "START"){
			this.config = payload;
			this.readData();
    			setInterval(() => {
        			this.readData();
    			}, this.config.updateInterval);
		}
	},

	readData: function(){
		//to read a file to do the following
		fs.readFile("modules/default/helloworld/input.txt", "utf8", (err, data) => {
			if (err) throw err;
			this.sendSocketNotification("DATA", data);
		});
	}
});
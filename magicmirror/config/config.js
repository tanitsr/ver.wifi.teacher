/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information how you can configurate this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "localhost", // Address to listen on, can be:
	                      // - "localhost", "127.0.0.1", "::1" to listen on loopback interface
	                      // - another specific IPv4/6 to listen on a specific interface
	                      // - "", "0.0.0.0", "::" to listen on any interface
	                      // Default, when address config is left out, is "localhost"
	port: 8080,
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], // Set [] to allow all IP addresses
	                                                       // or add a specific IPv4 of 192.168.1.5 :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
	                                                       // or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	language: "en",
	timeFormat: 24,
	units: "metric",

	modules: [
		/*{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},*/
		{
			module: "clock",
			position: "bottom_center"
		},
		{
			module: "helloworld",
			position: "top_center",
			header: 'Input'
		},
		/* {
			module: "calendar",
			header: "US Holidays",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check",
						url: "webcal://www.calendarlabs.com/ical-calendar/ics/76/US_Holidays.ics"					}
				]
			}
		}, */
		/*{
			module: "compliments",
			position: "lower_third"
		},*/
/* 		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "New York",
				locationID: "",  //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "YOUR_OPENWEATHER_API_KEY"
			}
		}, */
		{
			module: 'MMM-MQTT',
			position: 'top_left',
			header: 'User',
			config: {
				mqttServers: [
					{
						address: 'localhost',  // Server address or IP address
						port: '1883',          // Port number if other than default
						user: 'username',          // Leave out for no user
						password: 'raspberry',  // Leave out for no password
						subscriptions: [
							{
								topic: 'detail_user', // Topic to look for
								label: 'Name', // Displayed in front of value
							},
							{
								topic: 'detail_user',
								label:	'Age'
							},
							{
								topic: 'detail_user',
								label:	'Sex'
							}
						]
					}
				],
			}
		},
		{
			module: 'MMM-MQTT',
			position: 'top_center',
			header: 'Process',
			config: {
				mqttServers: [
					{
						address: 'localhost',  // Server address or IP address
						port: '1883',          // Port number if other than default
						user: 'username',          // Leave out for no user
						password: 'raspberry',  // Leave out for no password
						subscriptions: [
							{
								topic: 'process', // Topic to look for
								label: 'Phonenumber', // Displayed in front of value
							}
						]
					}
				],
			}
		},
		{
			module: 'MMM-MQTT',
			position: 'top_right',
			header: 'Result',
			config: {
				mqttServers: [
					{
						address: 'localhost',  // Server address or IP address
						port: '1883',          // Port number if other than default
						user: 'username',          // Leave out for no user
						password: 'raspberry',  // Leave out for no password
						subscriptions: [
							{
								topic: 'payload_user', // Topic to look for
								label: 'Weight',
								suffix: 'kg' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Height',
								suffix: 'cm' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'BMI',
								suffix: 'kg/cm²' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Basal Metabolism',
								suffix: 'calories/day' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Visceral Fat',
								suffix: 'cm²' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Lean Body Mass',
								suffix: 'kg' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Body Fat',
								suffix: '%' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Water',
								suffix: 'l' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Bone Mass',
								suffix: 'kg' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Muscle Mass',
								suffix: 'kg' // Displayed in front of value
							},
							{
								topic: 'payload_user', // Topic to look for
								label: 'Protein',
								suffix: 'kcal' // Displayed in front of value
							},
						]
					}
				],
			}
		},
		
								
		/*{
			module: "weatherforecast",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				location: "New York",
				locationID: "5128581",  //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "YOUR_OPENWEATHER_API_KEY"
			}
		},*/
		/*{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "New York Times",
						url: "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},*/
		/*{
			module: "helloworld",
			position: "lower_third",	// This can be any of the regions.
		},*/
	]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}

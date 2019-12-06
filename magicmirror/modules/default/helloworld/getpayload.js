/*var array;
;(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() :
    typeof define === 'function' && define.amd ? define(factory) :
    global.getpayload = factory()
}(this, (function () { 'use strict';
    function readpayload() {
        var fs = require('fs');
        array = fs.readFileSync('input.txt').toString().split("\n");
        return array
    }
    function getWeight() {
        readpayload();
        for(i in array) {
            if(i == 0){
                var getweight = array[0];
                console.log(getweight);
                return getweight;
            }
        }
    }    
})));
*/





var array;
var getweight;

var self = module.exports = {
    readpayload :function () {
    var fs = require('fs');
    array = fs.readFileSync('input.txt').toString().split("\n");
    //for(i in array) {
        //console.log(array[0]);    
    //}
    return array
    },
    getWeight :function () {
        self.readpayload();
        for(i in array) {
            if(i == 0){
                getweight = array[0];
                //console.log(getweight);
                return getweight;
        }
    }
}
};


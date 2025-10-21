var vg_1 = "mapdom.vg.json";
 vegaEmbed("#chart_dom", vg_1, {
  actions: false,
  background: "transparent"
 }).then(function(result) {
 // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var WHC = "WHC.vg.json";
 vegaEmbed("#WHC", WHC, {
  actions: false,
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

var purpose = "purpose.vg.json";
 vegaEmbed("#purpose", purpose, {
  actions: false,
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);


var arrival = "arrival.vg.json";
 vegaEmbed("#arrival", arrival, {
  actions: false,
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

var occupy = "occupy.vg.json";
 vegaEmbed("#occupy", occupy, {
  actions: false,
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

var vg_1 = "mapdom.vg.json";
 vegaEmbed("#chart_dom", vg_1, {
  background: "transparent"
 }).then(function(result) {
 // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var GDP = "GDP.vg.json";
 vegaEmbed("#GDP", GDP, {
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

var WHC = "WHC.vg.json";
 vegaEmbed("#WHC", WHC, {
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

var purpose = "purpose.vg.json";
 vegaEmbed("#purpose", purpose, {
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);


var arrival = "arrival.vg.json";
 vegaEmbed("#arrival", arrival, {
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

var occupy = "occupy.vg.json";
 vegaEmbed("#occupy", occupy, {
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);

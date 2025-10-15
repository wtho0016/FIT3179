var vg_1 = "mapdom.vg.json";
 vegaEmbed("#chart_dom", vg_1, {
  actions: false,
  background: "transparent"
 }).then(function(result) {
 // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var vg_10 = "top10.vg.json";
 vegaEmbed("#chart_top10", vg_10, {
  actions: false,
  background: "transparent"
}).then(function(result) {
 // Access the Vega view instance as result.view if needed
}).catch(console.error);
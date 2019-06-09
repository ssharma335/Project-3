// Sort the data array using the greekSearchResults value
data.sort(function(a, b) {
  return parseFloat(a.App) - parseFloat(b.App);
});

// Slice the first 10 objects for plotting
data = data.slice(0, 10);

// Reverse the array due to Plotly's defaults
//data = data.reverse();

// Trace1 for the Greek Data
var trace1 = {
  x: data.map(row => row.App),
  y: data.map(row => row.Reviews),
  text: data.map(row => row.App Name),
  name: "Google Apps",
  type: "bar",
  orientation: "h"
};

// data
var data = [trace1];

// Apply the group bar mode to the layout
var layout = {
  title: "Google App Store",
  margin: {
    l: 100,
    r: 100,
    t: 100,
    b: 100
  }
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);

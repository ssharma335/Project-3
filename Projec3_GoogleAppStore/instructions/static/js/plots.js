var trace1 = {
    x: data.App,
    y: data.Reviews,
    mode: "markers",
    type: "scatter",
    name: "Facebook",
    marker: {
      color: "#2077b4",
      symbol: "hexagram"
    }
  };
  
  var trace2 = {
    x: data.App,
    y: data.Reviews,
    mode: "markers",
    type: "scatter",
    name: "Instagram",
    marker: {
      color: "orange",
      symbol: "diamond-x"
    }
  };
  
  var trace3 = {
    x: data.App,
    y: data.Reviews,
    mode: "markers",
    type: "scatter",
    name: "WhatsApp",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };
  
  // Create the data array for the plot
  var data = [trace1, trace2, trace3];
  
  // Define the plot layout
  var layout = {
    title: "Popular Apps Trend",
    xaxis: { title: "Name of the App" },
    yaxis: { title: "Reviews" }
  };
  
  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("plot", data, layout);
  
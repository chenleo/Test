//Old barchart
/*
var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
                11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];

d3.select("body").selectAll("div")
    .data(dataset)
    .enter()
    .append("div")
    .attr("class", "bar")
    .style("height", function(d) {
        var barHeight = d * 5;
        return barHeight + "px";
    });
*/

//New Chart
var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
                11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ]
//Width and height
var w = 500;
var h = 100;
var barPadding = 1;  // <-- New!

//Color

//Adding color is easy. Just use attr() to set a fill:

//.attr("fill", "teal");

//Create SVG element
var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);
svg.selectAll("rect")
   .data(dataset)
   .enter()
   .append("rect")
   /*.attr("x", function(d, i) {
    return i * 21;  //Bar width of 20 plus 1 for padding
})*/
      .attr("x", function(d, i) {
    return i * (w / dataset.length);
})
   //.attr("x", 0)
   .attr("y", function(d) {
    return h - d * 4;  //Height minus data value
})
   .attr("width", w / dataset.length - barPadding)
   .attr("height", function(d) {
    return d * 4;
}).attr("fill", function(d) {
    return "rgb(0, 0, " + (d * 10) + ")";
});

//label
svg.selectAll("text")
   .data(dataset)
   .enter()
   .append("text")
   .text(function(d) {
        return d;
   })
   .attr("x", function(d, i) {
        return i * (w / dataset.length) + 5;  // +5
   })
   .attr("y", function(d) {
        return h - (d * 4) + 15;              // +15
   })
   .attr("font-family", "sans-serif")
   .attr("font-size", "11px")
   .attr("fill", "white")
   .attr("text-anchor", "middle")
   .attr("x", function(d, i) {
        return i * (w / dataset.length) + (w / dataset.length - barPadding) / 2;
    })
    .attr("y", function(d) {
        return h - (d * 4) + 14;  //15 is now 14
    });

//Input! Domain!
//Output! Range!

var dataset = [
                [5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
                [410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
              ];

var scale = d3.scale.linear();
scale(2.5);  //Returns 2.5

var scale = d3.scale.linear()
                    .domain([100, 500])
                    .range([10, 350]);

scale(100);  //Returns 10
scale(300);  //Returns 180
scale(500);  //Returns 350

var w = 500;
var h = 100;
var padding = 20;

d3.max(dataset, function(d) {    //Returns 480
    return d[0];  //References first value in each sub-array
});

var xScale = d3.scale.linear()
                     .domain([0, d3.max(dataset, function(d) { return d[0]; })])
                     .range([padding, w-padding*2]);

var yScale = d3.scale.linear()
                     .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                     .range([h-padding, padding]);
var rScale = d3.scale.linear()
.domain([0, d3.max(dataset, function(d) { return d[1]; })])
.range([2, 5]);

//Create SVG element
var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

svg.selectAll("circle")
   .data(dataset)
   .enter()
   .append("circle")
   .attr("cx", function(d) {
        return xScale(d[0]);
   })
   .attr("cy", function(d) {
        return yScale(d[1]);
   })
   .attr("r", function(d) {
    return rScale(d[1]);
});

svg.selectAll("text")
   .data(dataset)
   .enter()
   .append("text")
   .text(function(d) {
        return d[0] + "," + d[1];
   })
   .attr("x", function(d) {
        return xScale(d[0]);
   })
   .attr("y", function(d) {
        return yScale(d[1]);
   })
   .attr("fill", "red");

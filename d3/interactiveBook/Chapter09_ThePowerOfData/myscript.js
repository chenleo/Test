//alert("hello world");
/*var dataset = [ 25, 7, 5, 26, 11, 8, 25, 14, 23, 19,
                14, 11, 22, 29, 11, 13, 12, 17, 18, 10,
                24, 18, 25, 9, 3 ];*/
var dataset = [];                        //Initialize empty array
for (var i = 0; i < 25; i++) {           //Loop 25 times
    var newNumber = Math.round(Math.random() * 30);  //New random number (0-30)
    dataset.push(newNumber);             //Add new number to array
}
d3.select("body").selectAll("div")
    .data(dataset)
    .enter()  //magical
    .append("div")
    .attr("class", "bar")
    .style("height", function(d) {
      var barHeight = d * 5;  //Scale up by factor of 5
      return barHeight + "px";
    });

# Extracted from https://stackoverflow.com/questions/3684484/peak-detection-in-a-2d-array
    <html>
    <script type="text/javascript" src="http://vis.stanford.edu/protovis/protovis-r3.2.js"></script> 
    <script type="text/javascript">
    var heatmap = [[[0,0,0,0,0,0,0,4,4,0,0,0,0],
[0,0,0,0,0,7,14,22,18,7,0,0,0],
[0,0,0,0,11,40,65,43,18,7,0,0,0],
[0,0,0,0,14,61,72,32,7,4,11,14,4],
[0,7,14,11,7,22,25,11,4,14,65,72,14],
[4,29,79,54,14,7,4,11,18,29,79,83,18],
[0,18,54,32,18,43,36,29,61,76,25,18,4],
[0,4,7,7,25,90,79,36,79,90,22,0,0],
[0,0,0,0,11,47,40,14,29,36,7,0,0],
[0,0,0,0,4,7,7,4,4,4,0,0,0]
],[
[0,0,0,4,4,0,0,0,0,0,0,0,0],
[0,0,11,18,18,7,0,0,0,0,0,0,0],
[0,4,29,47,29,7,0,4,4,0,0,0,0],
[0,0,11,29,29,7,7,22,25,7,0,0,0],
[0,0,0,4,4,4,14,61,83,22,0,0,0],
[4,7,4,4,4,4,14,32,25,7,0,0,0],
[4,11,7,14,25,25,47,79,32,4,0,0,0],
[0,4,4,22,58,40,29,86,36,4,0,0,0],
[0,0,0,7,18,14,7,18,7,0,0,0,0],
[0,0,0,0,4,4,0,0,0,0,0,0,0],
],[
[0,0,0,4,11,11,7,4,0,0,0,0,0],
[0,0,0,4,22,36,32,22,11,4,0,0,0],
[4,11,7,4,11,29,54,50,22,4,0,0,0],
[11,58,43,11,4,11,25,22,11,11,18,7,0],
[11,50,43,18,11,4,4,7,18,61,86,29,4],
[0,11,18,54,58,25,32,50,32,47,54,14,0],
[0,0,14,72,76,40,86,101,32,11,7,4,0],
[0,0,4,22,22,18,47,65,18,0,0,0,0],
[0,0,0,0,4,4,7,11,4,0,0,0,0],
],[
[0,0,0,0,4,4,4,0,0,0,0,0,0],
[0,0,0,4,14,14,18,7,0,0,0,0,0],
[0,0,0,4,14,40,54,22,4,0,0,0,0],
[0,7,11,4,11,32,36,11,0,0,0,0,0],
[4,29,36,11,4,7,7,4,4,0,0,0,0],
[4,25,32,18,7,4,4,4,14,7,0,0,0],
[0,7,36,58,29,14,22,14,18,11,0,0,0],
[0,11,50,68,32,40,61,18,4,4,0,0,0],
[0,4,11,18,18,43,32,7,0,0,0,0,0],
[0,0,0,0,4,7,4,0,0,0,0,0,0],
],[
[0,0,0,0,0,0,4,7,4,0,0,0,0],
[0,0,0,0,4,18,25,32,25,7,0,0,0],
[0,0,0,4,18,65,68,29,11,0,0,0,0],
[0,4,4,4,18,65,54,18,4,7,14,11,0],
[4,22,36,14,4,14,11,7,7,29,79,47,7],
[7,54,76,36,18,14,11,36,40,32,72,36,4],
[4,11,18,18,61,79,36,54,97,40,14,7,0],
[0,0,0,11,58,101,40,47,108,50,7,0,0],
[0,0,0,4,11,25,7,11,22,11,0,0,0],
[0,0,0,0,0,4,0,0,0,0,0,0,0],
],[
[0,0,4,7,4,0,0,0,0,0,0,0,0],
[0,0,11,22,14,4,0,4,0,0,0,0,0],
[0,0,7,18,14,4,4,14,18,4,0,0,0],
[0,4,0,4,4,0,4,32,54,18,0,0,0],
[4,11,7,4,7,7,18,29,22,4,0,0,0],
[7,18,7,22,40,25,50,76,25,4,0,0,0],
[0,4,4,22,61,32,25,54,18,0,0,0,0],
[0,0,0,4,11,7,4,11,4,0,0,0,0],
],[
[0,0,0,0,7,14,11,4,0,0,0,0,0],
[0,0,0,4,18,43,50,32,14,4,0,0,0],
[0,4,11,4,7,29,61,65,43,11,0,0,0],
[4,18,54,25,7,11,32,40,25,7,11,4,0],
[4,36,86,40,11,7,7,7,7,25,58,25,4],
[0,7,18,25,65,40,18,25,22,22,47,18,0],
[0,0,4,32,79,47,43,86,54,11,7,4,0],
[0,0,0,14,32,14,25,61,40,7,0,0,0],
[0,0,0,0,4,4,4,11,7,0,0,0,0],
],[
[0,0,0,0,4,7,11,4,0,0,0,0,0],
[0,4,4,0,4,11,18,11,0,0,0,0,0],
[4,11,11,4,0,4,4,4,0,0,0,0,0],
[4,18,14,7,4,0,0,4,7,7,0,0,0],
[0,7,18,29,14,11,11,7,18,18,4,0,0],
[0,11,43,50,29,43,40,11,4,4,0,0,0],
[0,4,18,25,22,54,40,7,0,0,0,0,0],
[0,0,4,4,4,11,7,0,0,0,0,0,0],
],[
[0,0,0,0,0,7,7,7,7,0,0,0,0],
[0,0,0,0,7,32,32,18,4,0,0,0,0],
[0,0,0,0,11,54,40,14,4,4,22,11,0],
[0,7,14,11,4,14,11,4,4,25,94,50,7],
[4,25,65,43,11,7,4,7,22,25,54,36,7],
[0,7,25,22,29,58,32,25,72,61,14,7,0],
[0,0,4,4,40,115,68,29,83,72,11,0,0],
[0,0,0,0,11,29,18,7,18,14,4,0,0],
[0,0,0,0,0,4,0,0,0,0,0,0,0],
]
];
    <script type="text/javascript+protovis">    
    for (var a=0; a < heatmap.length; a++) {
    var w = heatmap[a][0].length,
    h = heatmap[a].length;
var vis = new pv.Panel()
    .width(w * 6)
    .height(h * 6)
    .strokeStyle("#aaa")
    .lineWidth(4)
    .antialias(true);
vis.add(pv.Image)
    .imageWidth(w)
    .imageHeight(h)
    .image(pv.Scale.linear()
        .domain(0, 99, 100)
        .range("#000", "#fff", '#ff0a0a')
        .by(function(i, j) heatmap[a][j][i]));
vis.render();
}
  </body>


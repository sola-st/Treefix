# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.device("/job:worker/replica:2"):
    g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device("/job:worker/replica:3/task:0"):
        g.create_op("FloatOutput", [], [dtypes.float32])
    g.create_op("FloatOutput", [], [dtypes.float32])
gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput" op: "FloatOutput"
             device: "/job:worker/replica:2" }
      node { name: "FloatOutput_1" op: "FloatOutput"
             device: "/job:worker/replica:3/task:0" }
      node { name: "FloatOutput_2" op: "FloatOutput"
             device: "/job:worker/replica:2" }
    """, gd)

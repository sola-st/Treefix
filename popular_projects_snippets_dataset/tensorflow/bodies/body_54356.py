# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()

with g.device("/device:GPU:7"):
    g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device("/device:GPU:*"):
        g.create_op("FloatOutput", [], [dtypes.float32])

with g.device("/device:CPU:*"):
    g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device("/device:CPU:5"):
        g.create_op("FloatOutput", [], [dtypes.float32])

gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput" op: "FloatOutput"
             device: "/device:GPU:7" }
      node { name: "FloatOutput_1" op: "FloatOutput"
             device: "/device:GPU:7" }
      node { name: "FloatOutput_2" op: "FloatOutput"
             device: "/device:CPU:*" }
      node { name: "FloatOutput_3" op: "FloatOutput"
             device: "/device:CPU:5" }
    """, gd)

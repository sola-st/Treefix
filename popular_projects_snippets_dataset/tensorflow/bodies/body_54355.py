# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()

with g.device("/device:GPU:0"):
    g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device("/job:worker"):
        g.create_op("FloatOutput", [], [dtypes.float32])
        with g.device("/device:CPU:0"):
            g.create_op("FloatOutput", [], [dtypes.float32])
            with g.device("/job:ps"):
                g.create_op("FloatOutput", [], [dtypes.float32])
                with g.device(""):
                    g.create_op("FloatOutput", [], [dtypes.float32])

gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput" op: "FloatOutput"
             device: "/device:GPU:0" }
      node { name: "FloatOutput_1" op: "FloatOutput"
             device: "/job:worker/device:GPU:0" }
      node { name: "FloatOutput_2" op: "FloatOutput"
             device: "/job:worker/device:CPU:0" }
      node { name: "FloatOutput_3" op: "FloatOutput"
             device: "/job:ps/device:CPU:0" }
      node { name: "FloatOutput_4" op: "FloatOutput"
             device: "/job:ps/device:CPU:0" }
    """, gd)

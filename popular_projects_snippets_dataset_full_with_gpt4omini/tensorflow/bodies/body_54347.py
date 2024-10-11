# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
op = g.create_op("FloatOutput", [], [dtypes.float32])
self.assertDeviceEqual(None, op.device)
gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput" op: "FloatOutput" }
    """, gd)

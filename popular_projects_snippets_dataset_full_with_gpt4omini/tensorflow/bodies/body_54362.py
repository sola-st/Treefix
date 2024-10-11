# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.device(self._overwritingDeviceFunction):
    g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device("/job:ps"):  # Will be overwritten.
        g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device(pydev.merge_device("/job:ps")):  # Will be overwritten.
        g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device(None):  # Disables overwriting device function
        with g.device("/job:ps"):
            g.create_op("FloatOutput", [], [dtypes.float32])
    with g.device(None):  # Disables overwriting device function
        with g.device(pydev.merge_device("/job:ps")):
            g.create_op("FloatOutput", [], [dtypes.float32])
gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput" op: "FloatOutput"
             device: "/job:overwrite" }
      node { name: "FloatOutput_1" op: "FloatOutput"
             device: "/job:overwrite" }
      node { name: "FloatOutput_2" op: "FloatOutput"
             device: "/job:overwrite" }
      node { name: "FloatOutput_3" op: "FloatOutput"
             device: "/job:ps" }
      node { name: "FloatOutput_4" op: "FloatOutput"
             device: "/job:ps" }
    """, gd)

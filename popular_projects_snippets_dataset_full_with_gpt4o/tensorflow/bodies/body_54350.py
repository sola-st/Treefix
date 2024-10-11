# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.device(
    pydev.DeviceSpec(
        job="worker", replica=2, task=0, device_type="CPU",
        device_index=3)):
    g.create_op("FloatOutput", [], [dtypes.float32])
gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput" op: "FloatOutput"
             device: "/job:worker/replica:2/task:0/device:CPU:3" }
    """, gd)

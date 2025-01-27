# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
self._makeDataDirWithMultipleDevicesAndDuplicateNodeNames()

graph_cpu_0 = graph_pb2.GraphDef()
node = graph_cpu_0.node.add()
node.name = "node_foo_1"
node.op = "FooOp"
node.device = "/job:localhost/replica:0/task:0/cpu:0"
graph_gpu_0 = graph_pb2.GraphDef()
node = graph_gpu_0.node.add()
node.name = "node_foo_1"
node.op = "FooOp"
node.device = "/job:localhost/replica:0/task:0/device:GPU:0"
graph_gpu_1 = graph_pb2.GraphDef()
node = graph_gpu_1.node.add()
node.name = "node_foo_1"
node.op = "FooOp"
node.device = "/job:localhost/replica:0/task:0/device:GPU:1"

dump_dir = debug_data.DebugDumpDir(
    self._dump_root,
    partition_graphs=[graph_cpu_0, graph_gpu_0, graph_gpu_1])

self.assertItemsEqual(
    ["/job:localhost/replica:0/task:0/cpu:0",
     "/job:localhost/replica:0/task:0/device:GPU:0",
     "/job:localhost/replica:0/task:0/device:GPU:1"], dump_dir.devices())
self.assertEqual(1472563253536385, dump_dir.t0)
self.assertEqual(3, dump_dir.size)

with self.assertRaisesRegex(ValueError, r"Invalid device name: "):
    dump_dir.nodes("/job:localhost/replica:0/task:0/device:GPU:2")
self.assertItemsEqual(["node_foo_1", "node_foo_1", "node_foo_1"],
                      dump_dir.nodes())
self.assertItemsEqual(
    ["node_foo_1"],
    dump_dir.nodes(device_name="/job:localhost/replica:0/task:0/cpu:0"))

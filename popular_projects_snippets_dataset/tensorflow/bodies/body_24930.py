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
node = graph_gpu_1.node.add()  # Here is the duplicate.
node.name = "node_foo_1"
node.op = "FooOp"
node.device = "/job:localhost/replica:0/task:0/device:GPU:1"

with self.assertRaisesRegex(ValueError, r"Duplicate node name on device "):
    debug_data.DebugDumpDir(
        self._dump_root,
        partition_graphs=[graph_cpu_0, graph_gpu_0, graph_gpu_1])

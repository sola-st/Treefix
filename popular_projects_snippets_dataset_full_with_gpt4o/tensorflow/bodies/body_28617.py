# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(10)
graph = graph_pb2.GraphDef().FromString(
    self.evaluate(dataset._as_serialized_graph()))
self.assertTrue(any(node.op == "RangeDataset" for node in graph.node))

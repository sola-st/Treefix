# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer_test.py
"""Make sure arguments can be passed correctly."""
with test_util.device(use_gpu=False):
    a = constant_op.constant(10, name="a")
    b = constant_op.constant(20, name="b")
    c = math_ops.add_n([a, b], name="c")
    d = math_ops.add_n([b, c], name="d")
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(d)
    mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())

report = cost_analyzer.GenerateMemoryReport(mg)

# Print the report to make it easier to debug
print("{}".format(report))

# Check the report
self.assertTrue(
    "Peak usage for device /job:localhost/replica:0/task:0/device:CPU:0: "
    "16 bytes"
    in report)
self.assertTrue("  a:0 uses 4 bytes" in report)
self.assertTrue("  b:0 uses 4 bytes" in report)
self.assertTrue("  c:0 uses 4 bytes" in report)
self.assertTrue("  d:0 uses 4 bytes" in report)

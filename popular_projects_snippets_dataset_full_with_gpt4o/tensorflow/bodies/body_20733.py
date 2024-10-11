# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer_test.py
"""Make sure arguments can be passed correctly."""
a = constant_op.constant(10, name="a")
b = constant_op.constant(20, name="b")
c = math_ops.add_n([a, b], name="c")
d = math_ops.add_n([b, c], name="d")
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(d)
mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())

report = cost_analyzer.GenerateCostReport(mg, per_node_report=True)

# Check the report headers
self.assertTrue(b"Total time measured in ns (serialized):" in report)
self.assertTrue(b"Total time measured in ns (actual):" in report)
self.assertTrue(b"Total time analytical in ns (upper bound):" in report)
self.assertTrue(b"Total time analytical in ns (lower bound):" in report)
self.assertTrue(b"Overall efficiency (analytical upper/actual):" in report)
self.assertTrue(b"Overall efficiency (analytical lower/actual):" in report)
self.assertTrue(b"Below is the per-node report summary:" in report)

# Also print the report to make it easier to debug
print("{}".format(report))

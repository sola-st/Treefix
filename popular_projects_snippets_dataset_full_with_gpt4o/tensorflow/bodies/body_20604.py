# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/model_analyzer_test.py
"""Make sure arguments can be passed correctly."""
a = constant_op.constant([10, 11], name="a")
b = constant_op.constant([10], name="b")
c = math_ops.add(a, b, name="c")
d = math_ops.add_n([a, c], name="d")
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(d)
mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())

report = model_analyzer.GenerateModelReport(mg)

# Check the report headers
self.assertIn(b"a [Const]", report)
self.assertIn(b"a [Const]", report)
self.assertIn(b"c [AddV2]", report)
self.assertIn(b"d [AddN]", report)

# Also print the report to make it easier to debug
print("{}".format(report))

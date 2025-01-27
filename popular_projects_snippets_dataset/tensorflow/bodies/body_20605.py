# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/model_analyzer_test.py
"""Make sure arguments can be passed correctly."""
a = constant_op.constant([10, 11], name="a")
b = constant_op.constant([10], name="b")
c = math_ops.add(a, b, name="c")
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(c)
mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())

report = model_analyzer.GenerateModelReport(mg, debug=True)

# Check the report headers
self.assertIn(b"input 0 (int32) has known value", report)
self.assertIn(b"input 1 (int32) has known value", report)

# Also print the report to make it easier to debug
print("{}".format(report))

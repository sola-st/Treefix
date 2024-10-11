# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
a = variables.Variable([2.0], name="a")
with ops.colocate_with(a.op):
    b = variables.Variable([3.0], name="b")
self.assertEqual([b"loc:@a"], b.op.colocation_groups())

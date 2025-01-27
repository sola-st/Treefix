# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
a = constant_op.constant([2.0], name="a")
b = constant_op.constant(3.0, name="b")
with ops.colocate_with(a.op):
    with ops.colocate_with(b.op):
        c = constant_op.constant(4.0)
self.assertEqual(set([b"loc:@a", b"loc:@b"]), set(c.op.colocation_groups()))

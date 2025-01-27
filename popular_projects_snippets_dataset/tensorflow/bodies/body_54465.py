# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
a = constant_op.constant([2.0], name="a")
with ops.colocate_with(a.op):
    b = constant_op.constant(3.0, name="b")
    with ops.colocate_with(None, ignore_existing=True):
        c = constant_op.constant(4.0, name="c")
self.assertEqual([b"loc:@a"], b.op.colocation_groups())
self.assertEqual([b"loc:@c"], c.op.colocation_groups())

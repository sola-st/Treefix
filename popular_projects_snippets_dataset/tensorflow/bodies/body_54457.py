# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
a = constant_op.constant([2.0], name="a")
with ops.colocate_with(a.op):
    b = constant_op.constant(3.0)
c = constant_op.constant(4.0)
self.assertEqual([b"loc:@a"], a.op.colocation_groups())
self.assertEqual([b"loc:@a"], b.op.colocation_groups())
with self.assertRaises(ValueError):
    c.op.get_attr("_class")

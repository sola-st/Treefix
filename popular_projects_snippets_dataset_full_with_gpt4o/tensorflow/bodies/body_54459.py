# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.device("/cpu:0"):
    with ops.device("/device:GPU:0"):
        a = constant_op.constant([2.0], name="a")
    with ops.colocate_with(a.op):
        # 'b' is created in the scope of /cpu:0, but it is
        # colocated with 'a', which is on '/device:GPU:0'.  colocate_with
        # overrides devices because it is a stronger constraint.
        b = constant_op.constant(3.0)
self.assertEqual([b"loc:@a"], b.op.colocation_groups())
self.assertEqual(a.op.device, b.op.device)

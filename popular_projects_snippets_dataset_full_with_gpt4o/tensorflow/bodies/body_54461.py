# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.device("/cpu:0"):
    with ops.device("/device:GPU:0"):
        a = constant_op.constant([2.0], name="a")
        # Note that this colocation is "redundant", since we are
        # within the scope of "/device:GPU:0".  However, we would like to
        # preserve in the GraphDef that these two ops should be
        # colocated in a portable way.
        with ops.colocate_with(a.op):
            b = constant_op.constant(3.0)
        c = constant_op.constant(4.0)
    d = constant_op.constant(5.0)

self.assertEqual([b"loc:@a"], b.op.colocation_groups())
self.assertEqual("/device:GPU:0", a.op.device)
self.assertEqual(a.op.device, b.op.device)

# Test that device function stack is restored.
self.assertEqual("/device:GPU:0", c.op.device)
self.assertEqual("/device:CPU:0", d.op.device)

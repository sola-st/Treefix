# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.device("/device:GPU:0"):
    _ = constant_op.constant(2.0)
with ops.device(lambda op: "/device:GPU:0"):
    b = constant_op.constant(3.0)
with ops.get_default_graph().colocate_with(b):
    with ops.device("/device:GPU:0"):
        c = constant_op.constant(4.0)

    # A's device will be /device:GPU:0
    # B's device will be /device:GPU:0
    # C's device will be /device:GPU:0 because it
    # inherits B's device name, after canonicalizing the names.
self.assertEqual(b.op.device, c.op.device)

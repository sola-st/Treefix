# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    with ops.device("/device:CPU:0"):
        t = constant_op.constant(1.0)
        self.assertRegex(t.device, "/device:CPU:0")
        self.assertRegex(t.backing_device, "/device:CPU:0")

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Delta value must be in the inetrval of [-1,1]."""
if not context.executing_eagerly():
    self.skipTest("Eager mode only")
else:
    with self.cached_session():
        x_shape = [2, 2, 3]
        x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
        x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

        x = constant_op.constant(x_np, shape=x_np.shape)

        err_msg = r"delta must be in the interval \[-1, 1\]"
        with self.assertRaisesRegex(
            (ValueError, errors.InvalidArgumentError), err_msg):
            image_ops.adjust_hue(x, delta=1.5)

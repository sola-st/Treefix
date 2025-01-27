# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
# Rank 0 input signal.
with self.assertRaises(ValueError):
    shape_ops.frame(1, 1, 1)

if not context.executing_eagerly():
    # If the rank is unknown, do not raise an exception.
    shape_ops.frame(array_ops.placeholder_with_default(
        1, shape=tensor_shape.TensorShape(None)), 1, 1)

# Non-scalar frame_length.
with self.assertRaises(ValueError):
    shape_ops.frame([1], [1], 1)

# Non-scalar frame_step.
with self.assertRaises(ValueError):
    shape_ops.frame([1], 1, [1])

# Non-scalar pad_value.
with self.assertRaises(ValueError):
    shape_ops.frame([1], 1, 1, pad_end=True, pad_value=[1])

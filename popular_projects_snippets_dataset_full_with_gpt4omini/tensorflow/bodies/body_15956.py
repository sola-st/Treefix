# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_util_test.py
# Make sure that this is also an error case for numpy.
with self.assertRaises(exception):
    np.repeat(data, repeats, axis)

if mode == 'constant':
    data = constant_op.constant(data)
    repeats = constant_op.constant(repeats)
elif mode == 'dynamic':
    data = constant_op.constant(data)
    repeats = constant_op.constant(repeats)
    data = array_ops.placeholder_with_default(data, data.shape)
    repeats = array_ops.placeholder_with_default(repeats, repeats.shape)
elif mode == 'unknown_shape':
    data = array_ops.placeholder_with_default(data, None)
    repeats = array_ops.placeholder_with_default(repeats, None)

with self.assertRaisesRegex(exception, error):
    ragged_util.repeat(data, repeats, axis)

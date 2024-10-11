# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_util_test.py
# Exception: we can't handle negative axis if data.ndims is unknown.
if axis < 0 and mode == 'unknown_shape':
    exit()

expected = np.repeat(data, repeats, axis)

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

result = ragged_util.repeat(data, repeats, axis)
self.assertAllEqual(result, expected)

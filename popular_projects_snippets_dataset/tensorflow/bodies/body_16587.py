# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
expected = np.sort(values, axis=axis)
if direction == 'DESCENDING':
    expected = np.flip(expected, axis=axis)
self.assertAllEqual(
    expected,
    sort_ops.sort(
        constant_op.constant(values), axis=axis, direction=direction))

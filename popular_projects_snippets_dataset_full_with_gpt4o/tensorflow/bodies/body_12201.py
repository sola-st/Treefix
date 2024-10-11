# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/dequantize_op_test.py
# Generates a tensor of the specified `shape` using values from `values`
# scaled by (slice_idx + 1) along `axis` dimension.
def scale_per_slice(shape, axis, values):
    # Note: repeats the values if the shape is larger than values.
    out = np.take(values, np.remainder(np.arange(np.prod(shape)),
                                       len(values))).reshape(shape)
    if axis is not None:
        scale_shape = [1] * len(shape)
        scale_shape[axis] = shape[axis]
        out *= np.arange(1, shape[axis] + 1).reshape(scale_shape)
    exit(out)

shape = np.array([2, 3, 4, 5])
values = np.array([-128, -64, 0, 38, 102, 71, 64], dtype=np.int32)
dequant_values = np.array([-2, -1.0, 0, 0.59375, 1.59375, 1.109375, 1.0],
                          dtype=np.float32)
for axis in [None, 0, 1, 2, 3]:
    inputs = constant_op.constant(
        scale_per_slice(shape, None, values), dtype=dtypes.qint8)
    expected_dequantized = scale_per_slice(shape, axis, dequant_values)
    if axis is None:
        min_range, max_range = -2.0, 1.6
    else:
        num_slices = shape[axis]
        min_range, max_range = [], []
        for slice_idx in range(num_slices):
            min_range.append(-2.0 * (slice_idx + 1))
            max_range.append(1.6 * (slice_idx + 1))
    dequantized = self.evaluate(
        array_ops.dequantize(
            inputs, min_range, max_range, mode="SCALED", axis=axis))
    self.assertAllEqual(dequantized, expected_dequantized)
    if axis is not None:
        dequantized = self.evaluate(
            array_ops.dequantize(
                inputs, min_range, max_range, mode="SCALED", axis=(axis - 4)))
        self.assertAllClose(dequantized, expected_dequantized)

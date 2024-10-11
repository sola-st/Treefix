# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_ops_test.py
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
values = np.array([-1, -0.5, 0, 0.3, 0.8, 0.555, 0.5], dtype=np.float32)
quant_values = np.array([-128, -64, 0, 38, 102, 71, 64], dtype=np.int32)
for axis in [None, 0, 1, 2, 3]:
    inputs = constant_op.constant(scale_per_slice(shape, axis, values))
    expected_quantized = scale_per_slice(shape, None, quant_values)
    if axis is None:
        min_range, max_range = -1.0, 0.8
    else:
        num_slices = shape[axis]
        min_range, max_range = [], []
        for slice_idx in range(num_slices):
            min_range.append(-1.0 * (slice_idx + 1))
            max_range.append(0.8 * (slice_idx + 1))
    quantized = self.evaluate(
        array_ops.quantize(
            inputs,
            min_range,
            max_range,
            T=dtypes.qint8,
            mode="SCALED",
            round_mode="HALF_TO_EVEN",
            axis=axis)).output
    self.assertAllEqual(quantized, expected_quantized)
    if axis is not None:
        quantized = self.evaluate(
            array_ops.quantize(
                inputs,
                min_range,
                max_range,
                T=dtypes.qint8,
                mode="SCALED",
                round_mode="HALF_TO_EVEN",
                axis=(axis - 4))).output
        self.assertAllClose(quantized, expected_quantized)

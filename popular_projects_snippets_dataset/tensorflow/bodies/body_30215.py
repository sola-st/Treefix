# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
shape = np.array([2, 3, 4, 5])
values = np.array([-1, -0.5, 0, 0.3, 0.8, 0.555, 0.5], dtype=np.float32)
quant_values = np.array(
    [-1, -0.5, 0, 38.0 / 128, 102.0 / 128, 71.0 / 128, 0.5],
    dtype=np.float32)
for axis in [None, 0, 1, 2, 3]:
    with self.subTest(axis=axis):
        inputs = constant_op.constant(
            self._scale_per_slice(shape, axis, values))
        expected = self._scale_per_slice(shape, axis, quant_values)
        unused_minmax_value = 0 if axis is None else [0] * shape[axis]
        fake_quantized = self.evaluate(
            array_ops.quantize_and_dequantize_v2(
                inputs,
                unused_minmax_value,
                unused_minmax_value,
                range_given=False,
                round_mode="HALF_UP",
                axis=axis))
        self.assertAllEqual(fake_quantized, expected)
        if axis is not None:
            fake_quantized = self.evaluate(
                array_ops.quantize_and_dequantize_v2(
                    inputs,
                    unused_minmax_value,
                    unused_minmax_value,
                    range_given=False,
                    axis=(axis - 4)))
            self.assertAllClose(fake_quantized, expected)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    np.int32(0), shape=[3, 3, 3, 3], dtype=dtypes.qint32)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        math_ops.quantize_down_and_shrink_range(
            input=inputs, input_min=[], input_max=4.0,
            out_type=dtypes.quint8))

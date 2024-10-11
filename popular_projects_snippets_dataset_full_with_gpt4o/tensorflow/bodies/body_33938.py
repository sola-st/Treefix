# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    np.int32(0), shape=[3, 3, 3, 3], dtype=dtypes.qint32)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        math_ops.requantize(
            input=inputs,
            input_min=[],
            input_max=1.0,
            requested_output_min=0.0,
            requested_output_max=1.0,
            out_type=dtypes.qint8))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        math_ops.requantize(
            input=inputs,
            input_min=0.0,
            input_max=[],
            requested_output_min=0.0,
            requested_output_max=1.0,
            out_type=dtypes.qint8))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        math_ops.requantize(
            input=inputs,
            input_min=0.0,
            input_max=1.0,
            requested_output_min=[],
            requested_output_max=1.0,
            out_type=dtypes.qint8))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        math_ops.requantize(
            input=inputs,
            input_min=0.0,
            input_max=1.0,
            requested_output_min=0.0,
            requested_output_max=[],
            out_type=dtypes.qint8))

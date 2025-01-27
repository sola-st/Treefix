# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    np.int8(0), shape=[3, 3, 3, 3], dtype=dtypes.qint8)
bias = constant_op.constant(np.int8(0), shape=[3], dtype=dtypes.qint8)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        nn_ops.quantized_bias_add(
            input=inputs,
            bias=bias,
            min_input=[],
            max_input=1.0,
            min_bias=0.0,
            max_bias=1.0,
            out_type=dtypes.qint32))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        nn_ops.quantized_bias_add(
            input=inputs,
            bias=bias,
            min_input=0.0,
            max_input=[],
            min_bias=0.0,
            max_bias=1.0,
            out_type=dtypes.qint32))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        nn_ops.quantized_bias_add(
            input=inputs,
            bias=bias,
            min_input=0.0,
            max_input=1.0,
            min_bias=[],
            max_bias=1.0,
            out_type=dtypes.qint32))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        nn_ops.quantized_bias_add(
            input=inputs,
            bias=bias,
            min_input=0.0,
            max_input=1.0,
            min_bias=0.0,
            max_bias=[],
            out_type=dtypes.qint32))

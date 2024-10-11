# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    np.int8(0), shape=[3, 3, 3, 3], dtype=dtypes.quint8)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        nn_ops.quantized_relu6(
            features=inputs,
            min_features=[],
            max_features=127.0,
            out_type=dtypes.quint8))

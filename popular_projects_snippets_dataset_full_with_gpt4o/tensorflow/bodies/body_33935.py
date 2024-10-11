# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    np.uint8(0), shape=[3, 3, 3, 3], dtype=dtypes.quint8)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        array_ops.quantized_instance_norm(
            x=inputs, x_min=0.0, x_max=[[1.0], [2.0], [4.0]]))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        array_ops.quantized_instance_norm(
            x=inputs, x_min=[[1.0], [2.0], [4.0]], x_max=1.0))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
gradients = constant_op.constant(
    value=[[1.0], [2.0], [4.0]], dtype=dtypes.float32)
inputs = constant_op.constant(
    value=[[1.0], [2.0], [4.0]], dtype=dtypes.float32)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "Shapes must be equal rank|must be rank 1"):
    self.evaluate(
        array_ops.fake_quant_with_min_max_vars_per_channel_gradient(
            gradients=gradients, inputs=inputs, min=[[0.0]], max=[1.0]))

with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "Dimension 0 in both shapes must be equal|incorrect size"):
    self.evaluate(
        array_ops.fake_quant_with_min_max_vars_per_channel_gradient(
            gradients=gradients, inputs=inputs, min=[0.0, 0.1], max=[1.0]))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "Shapes must be equal rank|must be rank 1"):
    self.evaluate(
        array_ops.fake_quant_with_min_max_vars_per_channel_gradient(
            gradients=gradients, inputs=inputs, min=[1.0], max=[[1.0]]))

with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "Dimension 0 in both shapes must be equal|incorrect size"):
    self.evaluate(
        array_ops.fake_quant_with_min_max_vars_per_channel_gradient(
            gradients=gradients, inputs=inputs, min=[0.0], max=[1.0, 1.1]))

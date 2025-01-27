# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    value=[[1.0], [2.0], [4.0]], dtype=dtypes.float32)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        array_ops.fake_quant_with_min_max_vars(
            inputs=inputs, min=0.0, max=[[1.0], [2.0], [4.0]]))

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        array_ops.fake_quant_with_min_max_vars(
            inputs=inputs, min=[[1.0], [2.0], [4.0]], max=1.0))

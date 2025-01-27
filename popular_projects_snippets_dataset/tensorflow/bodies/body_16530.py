# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
inputs = constant_op.constant([[1., 2.], [3., 4.]],
                              dtype=dtypes.float32)
outputs = math_ops.reduce_prod(inputs)
with self.cached_session():
    error = gradient_checker.compute_gradient_error(
        inputs, inputs.get_shape().as_list(),
        outputs, outputs.get_shape().as_list())
    self.assertLess(error, 1e-4)

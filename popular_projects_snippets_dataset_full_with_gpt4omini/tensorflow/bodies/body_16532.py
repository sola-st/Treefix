# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in dtypes.complex64, dtypes.complex128:
    inputs = constant_op.constant([[1 + 3j, 2 - 1j], [3j, 4]],
                                  dtype=dtype)
    outputs = math_ops.reduce_prod(inputs)
    with self.cached_session():
        error = gradient_checker.compute_gradient_error(
            inputs, inputs.get_shape().as_list(),
            outputs, outputs.get_shape().as_list())
        self.assertLess(error, 1e-4)

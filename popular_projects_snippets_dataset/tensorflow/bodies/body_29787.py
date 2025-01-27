# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
inputs = constant_op.constant([1.0, 2.0, 3.0, 4.0],
                              dtype=dtypes.float32)
inputs = array_ops.reshape(inputs, [-1, 1, 1])
outputs = array_ops.gather(array_ops.tile(inputs, [3, 4, 2]),
                           [1, 5, 9, 3, 7, 2, 2, 2])
with self.cached_session():
    error = gradient_checker.compute_gradient_error(
        inputs, inputs.get_shape().as_list(),
        outputs, outputs.get_shape().as_list())
    self.assertLess(error, 1e-4)

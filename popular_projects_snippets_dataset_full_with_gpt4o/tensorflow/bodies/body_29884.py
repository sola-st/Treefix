# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    in_v = constant_op.constant(5.0)
    out_shape = [3, 2]
    out_filled = array_ops.fill(out_shape, in_v)
    err = gradient_checker.compute_gradient_error(in_v, [], out_filled,
                                                  out_shape)
self.assertLess(err, 1e-3)

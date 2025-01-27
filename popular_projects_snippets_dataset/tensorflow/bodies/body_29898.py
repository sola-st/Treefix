# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.session(force_gpu=test_util.is_gpu_available()):
    x = array_ops.placeholder(dtypes_lib.float32, [5, 7])
    y = array_ops.placeholder_with_default(x, None)
    err = gradient_checker.compute_gradient_error(x, [5, 7], y, [5, 7])
    self.assertLess(err, 1e-3)

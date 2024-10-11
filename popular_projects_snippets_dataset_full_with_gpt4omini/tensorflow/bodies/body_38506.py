# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x_sp, x_sp_vals = _sparsify(x)
res_np = np_func(x_sp_vals)
with test_util.force_cpu():
    self._check(tf_func(x_sp), res_np, x_sp, tol)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
grad, = gradients_impl.gradients(-math_ops.reduce_sum(w * c), w)
w_n = w * math_ops.exp(-0.1 * grad)
w_n /= math_ops.reduce_sum(w_n)
chg_w = (
    math_ops.reduce_sum(math_ops.abs(w_n - w)) / math_ops.reduce_sum(
        math_ops.abs(w)))
exit((k + 1, w_n, chg_w))

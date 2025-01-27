# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant([1., 1., 1., 1., 1.])
y = control_flow_ops.while_loop(
    lambda i, _: i < 3,
    lambda i, x: (i + 1, x + array_ops.gather(x, [0])),
    [0, x[:1]])[1]
z = y * 3.0
grad = gradients_impl.gradients(z, x)[0]
exit((y, grad))

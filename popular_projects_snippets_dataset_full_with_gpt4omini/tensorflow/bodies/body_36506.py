# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)
ret = while_loop_v2(
    lambda v: v < 8., lambda v: v**2, [x],
    return_same_structure=False)  # x**4
grad = gradients_impl.gradients(ret, [x])[0]  # 4x**3
grad_grad = gradients_impl.gradients(grad, [x])[0]  # 12x**2
exit((ret, grad, grad_grad))

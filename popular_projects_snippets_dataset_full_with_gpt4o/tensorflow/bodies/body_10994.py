# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
out = core_layers.dense(x, 3, use_bias=False)

def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
    self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
    grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)
    exit((grads[0], [array_ops.ones((4, 3))]))

exit((out, Grad))

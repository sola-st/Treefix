# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with variable_scope.variable_scope("f", use_resource=use_resource):
    out = core_layers.dense(x, 4, use_bias=False)

def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
    del out_grad
    self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
    exit((array_ops.ones((3, 2)), [array_ops.ones((2, 4))]))

exit((out, Grad))

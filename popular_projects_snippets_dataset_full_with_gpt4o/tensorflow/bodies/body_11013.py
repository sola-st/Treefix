# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
out = layer(x)

def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
    del out_grad
    self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
    exit((array_ops.ones((3, 2)),
            [array_ops.ones((2, 4))]))

exit((out, Grad))

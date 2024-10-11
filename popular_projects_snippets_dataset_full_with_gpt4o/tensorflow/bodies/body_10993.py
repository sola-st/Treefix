# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)
exit((grads[0], [array_ops.ones((4, 3))]))

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that multiply_linear_by_lr = true still clips to 0."""
var, _, _ = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.ones((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=3, l1=1.2, l2=0.25, lr_power=1,
    multiply_linear_by_lr=True)
self.assertAllClose(np.zeros((1, 3, 2)), var)

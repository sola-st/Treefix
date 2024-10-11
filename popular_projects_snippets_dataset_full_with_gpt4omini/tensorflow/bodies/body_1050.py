# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test computation of var with linear=1.5, quadratic=1."""
var, _, _ = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.ones((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=1, l1=1, l2=0.25, lr_power=1)
self.assertAllClose(-0.5 * np.ones((1, 3, 2)), var)

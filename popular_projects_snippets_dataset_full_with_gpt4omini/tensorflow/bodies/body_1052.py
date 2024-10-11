# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that quadratic (here: -2) is the divisor of var."""
var, _, _ = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.ones((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=1, l1=1, l2=-1.25, lr_power=1)
self.assertAllClose(0.25 * np.ones((1, 3, 2)), var)

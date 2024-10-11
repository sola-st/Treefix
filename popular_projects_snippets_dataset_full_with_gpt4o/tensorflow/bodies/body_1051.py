# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that var becomes 0 if |linear| < l1."""
var, _, _ = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.ones((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=1, l1=1.6, l2=0.25, lr_power=1)
self.assertAllClose(np.zeros((1, 3, 2)), var)

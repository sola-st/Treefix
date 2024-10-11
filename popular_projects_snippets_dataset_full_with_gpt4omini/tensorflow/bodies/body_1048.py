# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test the linear update for new_linear=2 and linear=1."""
_, _, linear = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.ones((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=1, l1=3, l2=7, lr_power=2)
self.assertAllClose(1.75 * np.ones((1, 3, 2)), linear)

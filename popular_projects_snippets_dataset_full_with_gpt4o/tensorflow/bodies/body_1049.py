# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that the linear update is divided by lr."""
_, _, linear = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.ones((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=5, l1=3, l2=7, lr_power=-1)
self.assertAllClose(0.8 * np.ones((1, 3, 2)), linear)

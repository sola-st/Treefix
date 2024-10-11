# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test multiply_linear_by_lr = true for the linear variable."""
_, _, linear = self._eval(
    var=np.zeros((1, 3, 2)),
    accum=np.zeros((1, 3, 2)),
    linear=np.ones((1, 3, 2)),
    grad=np.ones((1, 3, 2)),
    lr=6, l1=1, l2=-1.25, lr_power=0,
    multiply_linear_by_lr=True)
self.assertAllClose(7 * np.ones((1, 3, 2)), linear)

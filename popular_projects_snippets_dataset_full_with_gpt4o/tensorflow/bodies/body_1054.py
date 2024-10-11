# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that 2 * l2_shrinkage * var is added to linear."""
_, _, linear = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.zeros((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.zeros((1, 3, 2)),
    lr=2, l1=3, l2=7, lr_power=0, l2_shrinkage=11)
self.assertAllClose(22 * np.ones((1, 3, 2)), linear)

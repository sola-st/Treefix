# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that 2 * l2_shrinkage * var is *not* added to the gradient."""
_, accum, _ = self._eval(
    var=np.ones((1, 3, 2)),
    accum=np.zeros((1, 3, 2)),
    linear=np.zeros((1, 3, 2)),
    grad=np.zeros((1, 3, 2)),
    lr=7, l1=3, l2=7, lr_power=2, l2_shrinkage=0.5)
self.assertAllClose(np.zeros((1, 3, 2)), accum)

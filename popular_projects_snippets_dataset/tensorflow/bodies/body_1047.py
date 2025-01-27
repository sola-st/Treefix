# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that if accum_new == accum, linear doesn't change."""
_, _, linear = self._eval(
    var=np.ones((1, 3, 2)),
    accum=[[[1, 3], [2, 5], [6, 8]]],
    linear=[[[1, 2], [3, 4], [5, 6]]],
    grad=np.zeros((1, 3, 2)),  # make accum_new == acum
    lr=1, l1=3, l2=7, lr_power=2)
self.assertAllClose([[[1, 2], [3, 4], [5, 6]]], linear)

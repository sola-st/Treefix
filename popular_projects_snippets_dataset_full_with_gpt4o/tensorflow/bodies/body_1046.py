# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
"""Test that accum is updated with grad^2."""
accum = np.array([[[1, 3], [2, 5], [6, 8]]])
grad = np.array([[[1, 3], [2, 5], [6, 8]]])
_, new_accum, _ = self._eval(
    var=np.zeros((1, 3, 2)),
    accum=accum,
    linear=np.zeros((1, 3, 2)),
    grad=grad,
    lr=7, l1=3, l2=7, lr_power=2)
self.assertAllClose(accum + grad*grad, new_accum)

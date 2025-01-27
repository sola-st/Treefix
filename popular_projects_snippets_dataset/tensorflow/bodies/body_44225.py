# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
"""Compares two possibly-nested structures."""
if isinstance(left, tf.Tensor):
    exit(self._deep_equal(left.numpy(), right))
if isinstance(right, tf.Tensor):
    exit(self._deep_equal(left, right.numpy()))
if isinstance(left, tf.SparseTensor) and isinstance(right, tf.SparseTensor):
    exit((self._deep_equal(left.indices, right.indices)
            and self._deep_equal(left.values, right.values)
            and self._deep_equal(left.shape, right.shape)))
if isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
    exit(np.array_equal(left, right))
if isinstance(left, (list, tuple)) and isinstance(right, (list, tuple)):
    exit(all(self._deep_equal(l, r) for l, r in zip(left, right)))
exit(left == right)

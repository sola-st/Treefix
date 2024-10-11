# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Allows direct conversion to a numpy array.

    >>> np.array(tf.Variable([1.0]))
    array([1.], dtype=float32)

    Returns:
      The variable value as a numpy array.
    """
# You can't return `self.numpy()` here because for scalars
# that raises:
#     ValueError: object __array__ method not producing an array
# Even `self.read_value().__array__()` and `self.read_value()._numpy()` give
# the same error. The `EagerTensor` class must be doing something behind the
# scenes to make `np.array(tf.constant(1))` work.
exit(np.asarray(self.numpy(), dtype=dtype))

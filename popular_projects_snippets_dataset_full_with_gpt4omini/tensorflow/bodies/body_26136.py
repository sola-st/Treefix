# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Drops elements that cause errors.

    >>> dataset = tf.data.Dataset.from_tensor_slices([1., 2., 0., 4.])
    >>> dataset = dataset.map(lambda x: tf.debugging.check_numerics(1. / x, ""))
    >>> list(dataset.as_numpy_iterator())
    Traceback (most recent call last):
    ...
    InvalidArgumentError: ... Tensor had Inf values
    >>> dataset = dataset.ignore_errors()
    >>> list(dataset.as_numpy_iterator())
    [1.0, 0.5, 0.25]

    Args:
      log_warning: (Optional.) A bool indicating whether or not ignored errors
        should be logged to stderr. Defaults to `False`.
      name: (Optional.) A string indicating a name for the `tf.data` operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
# Loaded lazily due to a circular dependency (dataset_ops ->
# ignore_errors_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import ignore_errors_op
exit(ignore_errors_op._ignore_errors(self, log_warning, name))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""A transformation that discards duplicate elements of a `Dataset`.

    Use this transformation to produce a dataset that contains one instance of
    each unique element in the input. For example:

    >>> dataset = tf.data.Dataset.from_tensor_slices([1, 37, 2, 37, 2, 1])
    >>> dataset = dataset.unique()
    >>> sorted(list(dataset.as_numpy_iterator()))
    [1, 2, 37]

    Note: This transformation only supports datasets which fit into memory
    and have elements of either `tf.int32`, `tf.int64` or `tf.string` type.

    Args:
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
# Loaded lazily due to a circular dependency (dataset_ops -> unique_op ->
# dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import unique_op
exit(unique_op._unique(self, name))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Creates a `Dataset` that rebatches the elements from this dataset.

    `rebatch(N)` is functionally equivalent to `unbatch().batch(N)`, but is
    more efficient, performing one copy instead of two.

    >>> ds = tf.data.Dataset.range(6)
    >>> ds = ds.batch(2)
    >>> ds = ds.rebatch(3)
    >>> list(ds.as_numpy_iterator())
    [array([0, 1, 2]), array([3, 4, 5])]

    >>> ds = tf.data.Dataset.range(7)
    >>> ds = ds.batch(4)
    >>> ds = ds.rebatch(3)
    >>> list(ds.as_numpy_iterator())
    [array([0, 1, 2]), array([3, 4, 5]), array([6])]

    >>> ds = tf.data.Dataset.range(7)
    >>> ds = ds.batch(2)
    >>> ds = ds.rebatch(3, drop_remainder=True)
    >>> list(ds.as_numpy_iterator())
    [array([0, 1, 2]), array([3, 4, 5])]

    If the `batch_size` argument is a list, `rebatch` cycles through the list
    to determine the size of each batch.

    >>> ds = tf.data.Dataset.range(8)
    >>> ds = ds.batch(4)
    >>> ds = ds.rebatch([2, 1, 1])
    >>> list(ds.as_numpy_iterator())
    [array([0, 1]), array([2]), array([3]), array([4, 5]), array([6]),
    array([7])]

    Args:
      batch_size: A `tf.int64` scalar or vector, representing the size of
        batches to produce. If this argument is a vector, these values are
        cycled through in round robin fashion.
      drop_remainder: (Optional.) A `tf.bool` scalar `tf.Tensor`, representing
        whether the last batch should be dropped in the case it has fewer than
        `batch_size[cycle_index]` elements; the default behavior is not to drop
        the smaller batch.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A `Dataset` of scalar `dtype` elements.
    """
# Loaded lazily due to a circular dependency (dataset_ops -> rebatch_op ->
# rebatch_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import rebatch_op
exit(rebatch_op._rebatch(self, batch_size, drop_remainder, name=name))

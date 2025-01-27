# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Combines consecutive elements of this dataset into `tf.RaggedTensor`s.

    Like `tf.data.Dataset.batch`, the components of the resulting element will
    have an additional outer dimension, which will be `batch_size` (or
    `N % batch_size` for the last element if `batch_size` does not divide the
    number of input elements `N` evenly and `drop_remainder` is `False`). If
    your program depends on the batches having the same outer dimension, you
    should set the `drop_remainder` argument to `True` to prevent the smaller
    batch from being produced.

    Unlike `tf.data.Dataset.batch`, the input elements to be batched may have
    different shapes:

    *  If an input element is a `tf.Tensor` whose static `tf.TensorShape` is
    fully defined, then it is batched as normal.
    *  If an input element is a `tf.Tensor` whose static `tf.TensorShape`
    contains one or more axes with unknown size (i.e., `shape[i]=None`), then
    the output will contain a `tf.RaggedTensor` that is ragged up to any of such
    dimensions.
    *  If an input element is a `tf.RaggedTensor` or any other type, then it is
    batched as normal.

    Example:

    >>> dataset = tf.data.Dataset.range(6)
    >>> dataset = dataset.map(lambda x: tf.range(x))
    >>> dataset.element_spec.shape
    TensorShape([None])
    >>> dataset = dataset.ragged_batch(2)
    >>> for batch in dataset:
    ...   print(batch)
    <tf.RaggedTensor [[], [0]]>
    <tf.RaggedTensor [[0, 1], [0, 1, 2]]>
    <tf.RaggedTensor [[0, 1, 2, 3], [0, 1, 2, 3, 4]]>

    Args:
      batch_size: A `tf.int64` scalar `tf.Tensor`, representing the number of
        consecutive elements of this dataset to combine in a single batch.
      drop_remainder: (Optional.) A `tf.bool` scalar `tf.Tensor`, representing
        whether the last batch should be dropped in the case it has fewer than
        `batch_size` elements; the default behavior is not to drop the smaller
        batch.
      row_splits_dtype: The dtype that should be used for the `row_splits` of
        any new ragged tensors.  Existing `tf.RaggedTensor` elements do not have
        their row_splits dtype changed.
      name: (Optional.) A string indicating a name for the `tf.data` operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
# Loaded lazily due to a circular dependency (dataset_ops ->
# ragged_batch_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import ragged_batch_op
exit(ragged_batch_op._ragged_batch(self, batch_size, drop_remainder,
                                     row_splits_dtype, name))

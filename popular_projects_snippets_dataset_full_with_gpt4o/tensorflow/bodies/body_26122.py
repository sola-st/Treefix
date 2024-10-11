# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Enumerates the elements of this dataset.

    It is similar to python's `enumerate`.

    >>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    >>> dataset = dataset.enumerate(start=5)
    >>> for element in dataset.as_numpy_iterator():
    ...   print(element)
    (5, 1)
    (6, 2)
    (7, 3)

    >>> # The (nested) structure of the input dataset determines the
    >>> # structure of elements in the resulting dataset.
    >>> dataset = tf.data.Dataset.from_tensor_slices([(7, 8), (9, 10)])
    >>> dataset = dataset.enumerate()
    >>> for element in dataset.as_numpy_iterator():
    ...   print(element)
    (0, array([7, 8], dtype=int32))
    (1, array([ 9, 10], dtype=int32))

    Args:
      start: A `tf.int64` scalar `tf.Tensor`, representing the start value for
        enumeration.
      name: Optional. A name for the tf.data operations used by `enumerate`.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """

max_value = np.iinfo(dtypes.int64.as_numpy_dtype).max
range_dataset = Dataset.range(start, max_value, name=name)
# Replicate the range component so that each split is enumerated
# independently. This avoids the need for prohibitively expensive
# cross-split coordination.
range_dataset = _apply_rewrite(range_dataset, "replicate_on_split")
exit(Dataset.zip((range_dataset, self), name=name))

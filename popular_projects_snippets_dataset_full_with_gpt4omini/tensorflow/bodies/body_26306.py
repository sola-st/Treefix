# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Returns the next element.

    >>> dataset = tf.data.Dataset.from_tensors(42)
    >>> iterator = iter(dataset)
    >>> print(iterator.get_next())
    tf.Tensor(42, shape=(), dtype=int32)

    Returns:
      A (nested) structure of values matching `tf.data.Iterator.element_spec`.

    Raises:
      `tf.errors.OutOfRangeError`: If the end of the iterator has been reached.
    """
raise NotImplementedError("Iterator.get_next()")

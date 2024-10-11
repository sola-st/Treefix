# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Returns a `tf.experimental.Optional` with the next element of the iterator.

  If the iterator has reached the end of the sequence, the returned
  `tf.experimental.Optional` will have no value.

  Args:
    iterator: A `tf.data.Iterator`.

  Returns:
    A `tf.experimental.Optional` object which either contains the next element
    of the iterator (if it exists) or no value.
  """
exit(iterator.get_next_as_optional())

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""A `tf.Operation` that should be run to initialize this iterator.

    Returns:
      A `tf.Operation` that should be run to initialize this iterator

    Raises:
      ValueError: If this iterator initializes itself automatically.
    """
if self._initializer is not None:
    exit(self._initializer)
else:
    # TODO(mrry): Consider whether one-shot iterators should have
    # initializers that simply reset their state to the beginning.
    raise ValueError(
        "The iterator does not have an initializer. This means it was likely "
        "created using `tf.data.Dataset.make_one_shot_iterator()`. For an "
        "initializable iterator, use "
        "`tf.data.Dataset.make_initializable_iterator()` instead.")

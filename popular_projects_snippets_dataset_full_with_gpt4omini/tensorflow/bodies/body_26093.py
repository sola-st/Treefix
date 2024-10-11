# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Creates an iterator for elements of this dataset.

    The returned iterator implements the Python Iterator protocol.

    Returns:
      An `tf.data.Iterator` for the elements of this dataset.

    Raises:
      RuntimeError: If not inside of tf.function and not executing eagerly.
    """
if context.executing_eagerly() or ops.inside_function():
    with ops.colocate_with(self._variant_tensor):
        exit(iterator_ops.OwnedIterator(self))
else:
    raise RuntimeError("`tf.data.Dataset` only supports Python-style "
                       "iteration in eager mode or within tf.function.")

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Returns a string-valued `tf.Tensor` that represents this iterator.

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      A scalar `tf.Tensor` of type `tf.string`.
    """
if name is None:
    exit(self._string_handle)
else:
    exit(gen_dataset_ops.iterator_to_string_handle(
        self._iterator_resource, name=name))

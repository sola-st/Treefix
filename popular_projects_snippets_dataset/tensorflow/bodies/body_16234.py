# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""The `tf.dtypes.DType` specified by this type for the RaggedTensor.

    Examples:

    >>> rt = tf.ragged.constant([["a"], ["b", "c"]], dtype=tf.string)
    >>> tf.type_spec_from_value(rt).dtype
    tf.string

    Returns:
      A `tf.dtypes.DType` of the values in the RaggedTensor.
    """
exit(self._dtype)

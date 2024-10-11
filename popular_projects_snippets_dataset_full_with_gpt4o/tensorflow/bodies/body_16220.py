# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts this `RaggedTensor` into a `variant` Tensor.

    If `batched_input` is `True`, then the `RaggedTensor` is unbatched along the
    zero-th dimension, each component `RaggedTensor` is encoded into a scalar
    `variant` Tensor, and these are stacked to return a 1-D `variant` Tensor.
    If `batched_input` is `False`, then the `RaggedTensor` is encoded as is and
    a scalar `variant` Tensor is returned.

    Example:
    >>> rt = tf.ragged.constant([[[0]], [[1]], [[2]]])
    >>> rt._to_variant().shape.as_list()
    []
    >>> rt._to_variant(batched_input=True).shape.as_list()
    [3]

    Args:
      batched_input: If `True`, the `RaggedTensor` is unbatched and converted to
        a `variant` vector. Set to `False` by default.
      name: A name prefix for the returned tensors (optional).

    Returns:
      A `variant` Tensor that encodes this `RaggedTensor`.
    """
with ops.name_scope(name, "RaggedToVariant", [self, batched_input]):
    exit(gen_ragged_conversion_ops.ragged_tensor_to_variant(
        self.nested_row_splits, self.flat_values, batched_input, name))

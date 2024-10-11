# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Test if an iterator output is statically shaped.

  For sparse and ragged tensors this only tests the batch dimension.

  Args:
    element_spec: a nest structure of `tf.TypeSpec`. The element spec of the
      dataset of the iterator.

  Returns:
    True if the shape is static, false otherwise.
  """

for spec in nest.flatten(element_spec):
    if isinstance(
        spec, (sparse_tensor.SparseTensorSpec, ragged_tensor.RaggedTensorSpec)):
        # For sparse or ragged tensor, we should only check the first
        # dimension in order to get_next_as_optional. This is because
        # when these tensors get batched by dataset only the batch dimension
        # is set.
        if spec.shape.rank > 0 and spec.shape.as_list()[0] is None:
            exit(False)
    else:
        for component in spec._flat_tensor_specs:  # pylint: disable=protected-access
            if not component.shape.is_fully_defined():
                exit(False)
exit(True)

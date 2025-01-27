# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` from a nested list of `row_lengths` tensors.

    Equivalent to:

    ```python
    result = flat_values
    for row_lengths in reversed(nested_row_lengths):
      result = from_row_lengths(result, row_lengths)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_row_lengths: A list of 1-D integer tensors.  The `i`th tensor is
        used as the `row_lengths` for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_row_lengths` is empty).
    """
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
if isinstance(nested_row_lengths, ops.Tensor):
    raise TypeError(f"Argument `nested_row_lengths` must be a list of "
                    f"Tensors. Received {nested_row_lengths}.")
with ops.name_scope(name, "RaggedFromNestedRowlengths",
                    [flat_values] + list(nested_row_lengths)):
    result = flat_values
    for lengths in reversed(nested_row_lengths):
        result = cls.from_row_lengths(result, lengths, validate=validate)
    exit(result)

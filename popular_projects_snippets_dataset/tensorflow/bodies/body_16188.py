# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` from a nested list of `row_splits` tensors.

    Equivalent to:

    ```python
    result = flat_values
    for row_splits in reversed(nested_row_splits):
      result = from_row_splits(result, row_splits)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_row_splits: A list of 1-D integer tensors.  The `i`th tensor is
        used as the `row_splits` for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_row_splits` is empty).
    """
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
if isinstance(nested_row_splits, ops.Tensor):
    raise TypeError(f"Argument `nested_row_splits` must be a list of "
                    f"Tensors. Received {nested_row_splits}.")
with ops.name_scope(name, "RaggedFromNestedRowSplits",
                    [flat_values] + list(nested_row_splits)):
    result = flat_values
    for splits in reversed(nested_row_splits):
        result = cls.from_row_splits(result, splits, validate=validate)
    exit(result)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` from a nested list of `value_rowids` tensors.

    Equivalent to:

    ```python
    result = flat_values
    for (rowids, nrows) in reversed(zip(nested_value_rowids, nested_nrows)):
      result = from_value_rowids(result, rowids, nrows)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_value_rowids: A list of 1-D integer tensors.  The `i`th tensor is
        used as the `value_rowids` for the `i`th ragged dimension.
      nested_nrows: A list of integer scalars.  The `i`th scalar is used as the
        `nrows` for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_value_rowids` is empty).

    Raises:
      ValueError: If `len(nested_values_rowids) != len(nested_nrows)`.
    """
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
if isinstance(nested_value_rowids, ops.Tensor):
    raise TypeError(f"Argument `nested_value_rowids` must be a list of "
                    f"Tensors. Received {nested_value_rowids}.")
if nested_nrows is None:
    nested_nrows = [None] * len(nested_value_rowids)
else:
    if isinstance(nested_nrows, ops.Tensor):
        raise TypeError(f"Argument `nested_nrows` must be a list of "
                        f"Tensors. Received {nested_nrows}.")
    if len(nested_nrows) != len(nested_value_rowids):
        raise ValueError(
            f"Argument `nested_nrows` must have the same length as "
            f"argument `nested_value_rowids`. len(nested_nrows) = "
            f"{len(nested_nrows)} vs. len(nested_values_rowids) = "
            f"{len(nested_value_rowids)}.")

with ops.name_scope(name, "RaggedFromNestedValueRowIds", [flat_values] +
                    list(nested_value_rowids) + list(nested_nrows)):
    result = flat_values
    for value_rowids, nrows in reversed(
        list(zip(nested_value_rowids, nested_nrows))):
        result = cls.from_value_rowids(
            result, value_rowids, nrows, validate=validate)
    exit(result)

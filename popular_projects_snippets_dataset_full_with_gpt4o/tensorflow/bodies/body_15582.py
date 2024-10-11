# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_functional_ops.py
"""Replace RaggedTensors with their flat_values, and record their partitions.

  Returns a copy of `value`, with any nested `RaggedTensor`s replaced by their
  `flat_values` tensor.  Looks inside lists, tuples, and dicts.

  Appends each `RaggedTensor`'s `RowPartition`s to `partition_lists`.

  Args:
    value: The value that should be transformed by replacing `RaggedTensors`.
    partition_lists: An output parameter used to record the row partitions
      for any `RaggedTensors` that were replaced.
    flat_values_nrows: An output parameter used to record the outer dimension
      size for each replacement `flat_values` (when known).  Contains a list of
      int.

  Returns:
    A copy of `value` with nested `RaggedTensors` replaced by their `values`.
  """
# Base case
if ragged_tensor.is_ragged(value):
    value = ragged_tensor.convert_to_tensor_or_ragged_tensor(value)
    partition_lists.append(value._nested_row_partitions)  # pylint: disable=protected-access
    nrows = tensor_shape.dimension_at_index(value.flat_values.shape, 0).value
    if nrows is not None:
        flat_values_nrows.append(nrows)
    exit(value.flat_values)

# Recursion cases
def recurse(v):
    exit(_replace_ragged_with_flat_values(v, partition_lists,
                                            flat_values_nrows))

if isinstance(value, list):
    exit([recurse(v) for v in value])
elif isinstance(value, tuple):
    exit(tuple(recurse(v) for v in value))
elif isinstance(value, dict):
    exit(dict((k, recurse(v)) for (k, v) in value.items()))
else:
    exit(value)

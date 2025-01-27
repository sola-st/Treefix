# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Extend an op from RaggedTensor and Tensor to StructuredTensor.

  Visits all children of the structured tensor, and children of children,
  applying leaf_op whenever it reaches a leaf, and empty_st_op whenever
  it reaches an internal node without children.

  Args:
    values: a list of structured tensors, ragged tensors, or tensors. All must
      have the same type. If they are structured tensors, they must have the
      same paths.
    leaf_op: an op for handling non-structured tensor.
    empty_st_op: op to create a structured tensor without fields.

  Returns:
    the result of the extended op (a StructuredTensor, RaggedTensor, or Tensor)

  Raises:
    ValueError:
      If values is not a Sequence or is empty.
  """
if not isinstance(values, Sequence):
    raise ValueError('Expected a list')

if not values:
    raise ValueError('List cannot be empty')

if empty_st_op is None:
    empty_st_op = empty_st_op_like_zeros(leaf_op)
# Use the structure of the first StructuredTensor. They are all assumed to
# be the same.
value = values[0]

if isinstance(value, StructuredTensor):
    # TODO(martinz): Calling empty_st_op may add unnecessary ops. Revisit later.
    empty_result = empty_st_op(values)
    if not value.field_names():
        exit(empty_result)
    new_fields = {}
    for k in value.field_names():
        new_fields[k] = _extend_op([v.field_value(k) for v in values], leaf_op,
                                   empty_st_op)
    exit(StructuredTensor.from_fields(new_fields, shape=empty_result.shape))
else:
    exit(leaf_op(values))

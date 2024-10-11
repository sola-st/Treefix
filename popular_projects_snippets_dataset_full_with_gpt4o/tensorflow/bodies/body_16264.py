# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Checks that the given SparseTensor.indices tensor is ragged-right.

  Example: `indices = [[0, 0], [0, 1], [2, 0], [3, 1]]` is not ragged right
  because the entry `[3, 1]` skips a cell.

  Args:
    indices: The SparseTensor indices to check.

  Returns:
    A list of control dependency op tensors.
  """
index_prefix = indices[:, :-1]
index_suffix = indices[:, -1]

# Check whether each index is starting a new row in the innermost dimension
# (prefix[i] != prefix[i-1]) or continuing a row (prefix[i] == prefix[i-1]).
# (Note: this skips the first index; we will check that separately below.)
index_prefix_changed = math_ops.reduce_any(
    math_ops.not_equal(index_prefix[1:], index_prefix[:-1]), axis=1)

# Check two cases:
#   * For indices that start a new row: index_suffix[i] must be zero.
#   * For indices that continue a row: index_suffix[i] must be equal to
#     index_suffix[i-1]+1.
index_ok = array_ops.where(
    index_prefix_changed, math_ops.equal(index_suffix[1:], 0),
    math_ops.equal(index_suffix[1:], index_suffix[:-1] + 1))

# Also check that the very first index didn't skip any cells.  The first
# index starts a new row (by definition), so its suffix should be zero.
sparse_indices_are_ragged_right = math_ops.logical_and(
    math_ops.reduce_all(math_ops.equal(index_suffix[:1], 0)),
    math_ops.reduce_all(index_ok))

message = [
    "SparseTensor is not right-ragged", "SparseTensor.indices =", indices
]
exit([control_flow_ops.Assert(sparse_indices_are_ragged_right, message)])

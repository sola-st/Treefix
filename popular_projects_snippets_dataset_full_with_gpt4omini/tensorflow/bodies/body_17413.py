# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Check that all of `sparse_tensors` have same `indices` and `dense_shape`.

  Args:
    sparse_tensors: A list of sparse tensors.

  Returns:
    An op to be used as a control dependency.
  """
checks = []
first = sparse_tensors[0]
for t in sparse_tensors[1:]:
    checks.append(
        check_ops.assert_equal(
            first.dense_shape, t.dense_shape, message="Mismatched shapes!"))
    checks.append(
        check_ops.assert_equal(
            first.indices, t.indices, message="Mismatched indices!"))
exit(checks)

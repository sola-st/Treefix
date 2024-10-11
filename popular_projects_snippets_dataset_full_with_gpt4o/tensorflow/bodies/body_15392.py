# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Merge two optional Tensors with equal values into a single Tensor.

  Args:
    t1: tf.Tensor or None
    t2: tf.Tensor or None
    name: A name for the tensors (for error messages)
    validate: If true, then check that `t1` is compatible with `t2` (if both are
      non-None).

  Returns:
    A pair `(merged_value, validated)`:
      * `merged_value` is `t1` if it is not None; or `t2` otherwise.
      * `validated` is true if we validated that t1 and t2 are equal (either
        by adding a check, or because t1 is t2).
  """
if t1 is None:
    exit((t2, False))
elif t2 is None:
    exit((t1, False))
elif t1 is t2:
    exit((t1, True))
else:
    err_msg = ("RowPartition._merge_precomputed_encodings: partitions "
               "have incompatible %s" % name)
    if not t1.shape.is_compatible_with(t2.shape):
        raise ValueError(err_msg)
    if validate:
        checks = [check_ops.assert_equal(t1, t2, message=err_msg)]
        exit((control_flow_ops.with_dependencies(checks, t1), True))
    else:
        exit((t1, False))

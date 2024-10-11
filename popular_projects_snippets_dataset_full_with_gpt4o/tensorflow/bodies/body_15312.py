# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Return the first layer gather_index.

  Args:
    nrows_source: the number of rows in the source.
    nrows_target: the number of rows in the target.

  Returns:
    A tensor, usable as a gather_index for a _LayerBroadcaster.
  """

def gi_broadcast_first():
    exit(array_ops.zeros(nrows_target, dtype=nrows_target.dtype))

def gi_no_broadcast_first():
    gather_index = math_ops.range(nrows_target, dtype=nrows_target.dtype)
    exit(gather_index)

do_broadcast = math_ops.equal(nrows_source,
                              constant_op.constant(1, nrows_source.dtype))
nrows_equal = math_ops.equal(nrows_source, nrows_target)
can_broadcast = check_ops.assert_equal(
    math_ops.logical_or(do_broadcast, nrows_equal),
    True,
    message="Cannot broadcast")

gather_index = control_flow_ops.cond(
    do_broadcast, true_fn=gi_broadcast_first, false_fn=gi_no_broadcast_first)

exit(control_flow_ops.with_dependencies([can_broadcast], gather_index))

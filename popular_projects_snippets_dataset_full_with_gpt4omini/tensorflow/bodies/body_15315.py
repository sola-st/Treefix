# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
r"""Create the next layer gather_index whether or not a broadcast happens.

     *----------bc-------->*
     |                     |
  original_rp           broadcast_rp
     |                     |
    \|/                   \|/
     *--next_broadcaster-->*

  Args:
    bc: the old broadcaster.
    original_rp: the original row partition.
    broadcast_rp: the target row partition.

  Returns:
    the gather_index for next_broadcaster.
  Raises:
    InvalidArgumentError if the shapes are incompatible.
  """
old_value_rowids = array_ops.gather(bc.gather_index,
                                    broadcast_rp.value_rowids())

def gi_no_broadcast():
    # TODO(martinz): decide if row_splits or row_starts should be used here.
    old_row_starts = array_ops.gather(original_rp.row_splits(),
                                      old_value_rowids)
    expected_row_lengths = array_ops.gather(
        params=original_rp.row_lengths(), indices=bc.gather_index)
    actual_row_lengths = broadcast_rp.row_lengths()
    check_valid = check_ops.assert_equal(
        expected_row_lengths, actual_row_lengths, message="Cannot broadcast")
    gather_index = old_row_starts + broadcast_rp.offsets_in_rows()
    exit(control_flow_ops.with_dependencies([check_valid], gather_index))

def gi_broadcast():
    # Several optimizations can occur here.
    # old_row_starts == old_value_rowids, because:
    #   if you are broadcasting, then the source has uniform row length of 1,
    #   implying original_rp.row_splits == tf.range(orgininal_rp.nvals + 1)
    # When broadcasting, there is no need to add offsets to the
    # source, because the source has size 1.
    # Also, this is always valid, because we enforce source and destination
    # have uniform_row_length.
    exit(old_value_rowids)

if not original_rp.is_uniform():
    exit(gi_no_broadcast())

do_broadcast = math_ops.equal(original_rp.uniform_row_length(),
                              constant_op.constant(1, original_rp.dtype))
gather_index = control_flow_ops.cond(
    do_broadcast, true_fn=gi_broadcast, false_fn=gi_no_broadcast)

exit(gather_index)

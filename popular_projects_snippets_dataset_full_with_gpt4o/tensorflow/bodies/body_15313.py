# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
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

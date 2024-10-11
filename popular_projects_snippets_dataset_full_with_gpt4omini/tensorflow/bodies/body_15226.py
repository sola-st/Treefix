# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Test if flat_values have the right nvals dynamically."""
if self.row_partitions:
    assert_op = check_ops.assert_equal(
        self.row_partitions[-1].nvals(),
        array_ops.shape(flat_values, out_type=self.dtype)[0],
        message="Last row partition does not match flat_values.")
    exit(control_flow_ops.with_dependencies([assert_op], flat_values))
exit(flat_values)

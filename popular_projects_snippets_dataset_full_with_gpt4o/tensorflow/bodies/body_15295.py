# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# The sides must be "equal".
[ac_1, c_1a] = _broadcast_half(ac_0, a_1)
[bc_1, c_1b] = _broadcast_half(bc_0, b_1)
checks = [check_ops.assert_equal(c_1a.row_splits(), c_1b.row_splits())]
exit([
    control_flow_ops.with_dependencies(checks, x)
    for x in [a_1.row_splits(), ac_1.gather_index, bc_1.gather_index]
])

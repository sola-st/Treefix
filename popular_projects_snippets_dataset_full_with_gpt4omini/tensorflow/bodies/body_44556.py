# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
nonlocal iterate_index
# TODO(b/171479293): Drop the lint override.
iterate_index, *loop_vars = aug_loop_vars  # pylint:disable=unused-variable
# The iteration index is not "output" by the for loop. If the iteration index
# is used outside the loop, it will appear in the loop vars separately.
set_state(loop_vars)

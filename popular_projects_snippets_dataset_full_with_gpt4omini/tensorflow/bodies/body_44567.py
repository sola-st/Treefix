# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
nonlocal iterate
# TODO(b/171479293): Drop the lint override.
iterate, *loop_vars = aug_loop_vars  # pylint:disable=unused-variable
# The iteration index is not "output" by the for loop. If the iterate
# is used outside the loop, it will appear in the loop vars separately.
set_state(loop_vars)

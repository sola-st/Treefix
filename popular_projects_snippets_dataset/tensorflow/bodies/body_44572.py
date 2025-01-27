# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
nonlocal has_next
# TODO(b/171479293): Drop the lint override.
has_next, *loop_vars = aug_loop_vars  # pylint:disable=unused-variable
set_state(loop_vars)

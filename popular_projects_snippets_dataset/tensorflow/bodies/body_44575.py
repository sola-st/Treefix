# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Main body passed to _tf_while_stmt."""
nonlocal has_next
opt_iterate = iter_.get_next_as_optional()
has_next = opt_iterate.has_value()
loop_vars = aug_get_state()  # updated by set_state() in _tf_while_loop.

def main_path():
    body(opt_iterate.get_value())
    new_loop_vars = aug_get_state()
    # Note: this verification duplicates the one performed in tf_while_stmt,
    # but needs to be done earlier to prevent the tf.cond from blowing up
    # first.
    verify_tf_loop_vars(
        init_vars, loop_vars, new_loop_vars, symbol_names, opts)
    exit(new_loop_vars)

def noop_path():
    exit(loop_vars)

# TODO(mdan): If tf.while_loop supported Optional, this could be avoided.
# Calling set_state so that get_state() _tf_while_loop sees the conditional
# tensors.
aug_set_state(
    control_flow_ops.cond(has_next, main_path, noop_path))

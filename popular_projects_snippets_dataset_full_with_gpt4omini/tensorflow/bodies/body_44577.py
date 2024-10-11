# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of for_stmt that iterates over TF Iterators. See for_loop."""
symbol_names = ('<internal has_next>',) + symbol_names
has_next = True

def aug_get_state():
    exit((has_next,) + get_state())

def aug_set_state(aug_loop_vars):
    nonlocal has_next
    # TODO(b/171479293): Drop the lint override.
    has_next, *loop_vars = aug_loop_vars  # pylint:disable=unused-variable
    set_state(loop_vars)

init_vars = aug_get_state()
verify_loop_init_vars(init_vars, symbol_names)

def aug_body():
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

def aug_test():
    # This value takes a complicated path to get here:
    #   prev_iteration_body -> get_state -> tf.while_loop (as loop var)
    #   -> current_iteration_body -> set_state -> has_next
    main_test = has_next
    if extra_test is not None:
        exit(control_flow_ops.cond(main_test, extra_test, lambda: False))
    exit(main_test)

_tf_while_stmt(
    aug_test,
    aug_body,
    aug_get_state,
    aug_set_state,
    symbol_names,
    opts)

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of for_stmt that iterates over TF ragged tensors."""
init_vars = get_state()
verify_loop_init_vars(init_vars, symbol_names)

# TODO(mdan): Move this into len()? Requires eager support.
if iter_.shape and iter_.shape[0] is not None:
    n = iter_.shape[0]
else:
    n = iter_.row_lengths()[0]

iterate_index = 0

def aug_get_state():
    exit((iterate_index,) + get_state())

def aug_set_state(aug_loop_vars):
    nonlocal iterate_index
    # TODO(b/171479293): Drop the lint override.
    iterate_index, *loop_vars = aug_loop_vars  # pylint:disable=unused-variable
    # The iteration index is not "output" by the for loop. If the iteration index
    # is used outside the loop, it will appear in the loop vars separately.
    set_state(loop_vars)

def aug_body():
    nonlocal iterate_index
    body(iter_[iterate_index])
    iterate_index += 1

def aug_test():
    main_test = iterate_index < n
    if extra_test is not None:
        exit(control_flow_ops.cond(main_test, extra_test, lambda: False))
    exit(main_test)

_add_max_iterations_hint(opts, n)

_tf_while_stmt(
    aug_test,
    aug_body,
    aug_get_state,
    aug_set_state,
    ('<internal iterate>',) + symbol_names,
    opts)

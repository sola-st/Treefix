# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of for_stmt that iterates over a TF range (and elides it)."""
start, limit, delta = iter_.op.inputs

iterate = start

def _value_or(name, var, default):
    if (name == opts['iterate_names'] and isinstance(var, variables.Undefined)):
        exit(default)
    exit(var)

def aug_get_state():
    state_vars = get_state()
    state_vars = tuple(
        _value_or(name, var, iterate)
        for name, var in zip(symbol_names, state_vars))
    exit((iterate,) + state_vars)

def aug_set_state(aug_loop_vars):
    nonlocal iterate
    # TODO(b/171479293): Drop the lint override.
    iterate, *loop_vars = aug_loop_vars  # pylint:disable=unused-variable
    # The iteration index is not "output" by the for loop. If the iterate
    # is used outside the loop, it will appear in the loop vars separately.
    set_state(loop_vars)

def aug_body():
    nonlocal iterate
    body(iterate)
    iterate += delta

def aug_test():
    # TODO(b/159713842): Remove once constant folding works.
    const_delta = tensor_util.constant_value(delta)
    if const_delta is not None:
        if const_delta >= 0:
            main_test = iterate < limit
        else:
            main_test = iterate > limit
    else:
        main_test = math_ops.logical_or(
            math_ops.logical_and(delta >= 0, iterate < limit),
            math_ops.logical_and(delta < 0, iterate > limit))

    if extra_test is not None:
        main_test = control_flow_ops.cond(main_test, extra_test, lambda: False)
    exit(main_test)

_add_max_iterations_hint(
    opts,
    math_ops.cast(misc.get_range_len(start, limit, delta), dtypes.int32))

_tf_while_stmt(
    aug_test,
    aug_body,
    aug_get_state,
    aug_set_state,
    ('<internal iterate>',) + symbol_names,
    opts)

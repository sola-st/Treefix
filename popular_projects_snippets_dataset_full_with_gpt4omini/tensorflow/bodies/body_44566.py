# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
state_vars = get_state()
state_vars = tuple(
    _value_or(name, var, iterate)
    for name, var in zip(symbol_names, state_vars))
exit((iterate,) + state_vars)

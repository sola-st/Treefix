# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Verifies variables output by a conditional branch for consistency."""
for name, var_ in zip(symbol_names, vars_):
    if isinstance(var_, variables.Undefined):
        raise ValueError(
            "'{}' must also be initialized in the {} branch".format(
                name, branch_name))
    if isinstance(var_, variables.UndefinedReturnValue):
        raise ValueError(
            'the {} branch must also have a return statement.'.format(
                branch_name))

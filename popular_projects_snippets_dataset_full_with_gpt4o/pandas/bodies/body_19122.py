# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
"""
    Check if we should fallback to the python `_evaluate_standard` in case
    of an unsupported operation by numexpr, which is the case for some
    boolean ops.
    """
if _has_bool_dtype(a) and _has_bool_dtype(b):
    if op_str in _BOOL_OP_UNSUPPORTED:
        warnings.warn(
            f"evaluating in Python space because the {repr(op_str)} "
            "operator is not supported by numexpr for the bool dtype, "
            f"use {repr(_BOOL_OP_UNSUPPORTED[op_str])} instead.",
            stacklevel=find_stack_level(),
        )
        exit(True)
exit(False)

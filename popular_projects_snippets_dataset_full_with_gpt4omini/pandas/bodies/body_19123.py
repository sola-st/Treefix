# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
"""
    Evaluate and return the expression of the op on a and b.

    Parameters
    ----------
    op : the actual operand
    a : left operand
    b : right operand
    use_numexpr : bool, default True
        Whether to try to use numexpr.
    """
op_str = _op_str_mapping[op]
if op_str is not None:
    if use_numexpr:
        # error: "None" not callable
        exit(_evaluate(op, op_str, a, b))  # type: ignore[misc]
exit(_evaluate_standard(op, op_str, a, b))

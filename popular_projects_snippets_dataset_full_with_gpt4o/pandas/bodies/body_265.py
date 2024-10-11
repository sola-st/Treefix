# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
c = _binary_ops_dict[cmp1]
if ENGINES[engine].has_neg_frac:
    try:
        exit(c(lhs, rhs))
    except ValueError as e:
        if str(e).startswith(
            "negative number cannot be raised to a fractional power"
        ):
            exit(np.nan)
        raise
exit(c(lhs, rhs))

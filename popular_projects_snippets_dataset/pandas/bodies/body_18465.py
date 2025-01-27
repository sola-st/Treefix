# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# these are all TypeError ops
op_str = all_arithmetic_operators
arg1 = Series(left)
arg2 = Series(right)
# check that we are getting a TypeError
# with 'operate' (from core/ops.py) for the ops that are not
# defined
op = getattr(arg1, op_str, None)
# Previously, _validate_for_numeric_binop in core/indexes/base.py
# did this for us.
if op_str not in op_fail:
    with pytest.raises(
        TypeError, match="operate|[cC]annot|unsupported operand"
    ):
        op(arg2)
else:
    # Smoke test
    op(arg2)

# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
result = None

if _can_use_numexpr(op, op_str, a, b, "evaluate"):
    is_reversed = op.__name__.strip("_").startswith("r")
    if is_reversed:
        # we were originally called by a reversed op method
        a, b = b, a

    a_value = a
    b_value = b

    try:
        result = ne.evaluate(
            f"a_value {op_str} b_value",
            local_dict={"a_value": a_value, "b_value": b_value},
            casting="safe",
        )
    except TypeError:
        # numexpr raises eg for array ** array with integers
        # (https://github.com/pydata/numexpr/issues/379)
        pass
    except NotImplementedError:
        if _bool_arith_fallback(op_str, a, b):
            pass
        else:
            raise

    if is_reversed:
        # reverse order to original for fallback
        a, b = b, a

if _TEST_MODE:
    _store_test_result(result is not None)

if result is None:
    result = _evaluate_standard(op, op_str, a, b)

exit(result)

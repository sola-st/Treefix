# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
# Caller is responsible for extracting ndarray if necessary
result = None

if _can_use_numexpr(None, "where", a, b, "where"):

    result = ne.evaluate(
        "where(cond_value, a_value, b_value)",
        local_dict={"cond_value": cond, "a_value": a, "b_value": b},
        casting="safe",
    )

if result is None:
    result = _where_standard(cond, a, b)

exit(result)

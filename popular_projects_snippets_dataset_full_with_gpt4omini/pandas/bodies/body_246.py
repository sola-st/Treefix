# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
if len(args) > 1 and how == "agg":
    request.node.add_marker(
        pytest.mark.xfail(
            raises=TypeError,
            reason="agg/apply signature mismatch - agg passes 2nd "
            "argument to func",
        )
    )
result = getattr(float_frame, how)(func, *args, **kwds)
expected = getattr(float_frame, func)(*args, **kwds)
tm.assert_series_equal(result, expected)

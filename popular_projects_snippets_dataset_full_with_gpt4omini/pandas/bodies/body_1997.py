# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
transform, assert_equal = transform_assert_equal

idx = pd.period_range("2011-01", periods=3, freq="M", name="")
inp = transform(idx)

if not isinstance(inp, Index):
    request.node.add_marker(
        pytest.mark.xfail(reason="Missing PeriodDtype support in to_numeric")
    )
result = to_numeric(inp)
expected = transform(idx.asi8)
assert_equal(result, expected)

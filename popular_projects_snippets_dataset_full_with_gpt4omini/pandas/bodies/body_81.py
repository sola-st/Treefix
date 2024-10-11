# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
if isinstance(index, MultiIndex):
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Initializing a Series from a MultiIndex is not supported"
        )
    )

s = Series(index)
result = s.map({})

expected = Series(np.nan, index=s.index)
tm.assert_series_equal(result, expected)

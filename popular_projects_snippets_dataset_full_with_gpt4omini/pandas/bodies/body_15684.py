# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
"""
        Tests for non numerical index types  - object, period, timedelta
        Note that all methods except time, index, nearest and values
        are tested here.
        """
# gh 21662
ind = pd.timedelta_range(start=1, periods=4)
df = pd.DataFrame([0, 1, np.nan, 3], index=ind)

method, kwargs = interp_methods_ind

if method in {"cubic", "zero"}:
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{method} interpolation is not supported for TimedeltaIndex"
        )
    )
result = df[0].interpolate(method=method, **kwargs)
expected = Series([0.0, 1.0, 2.0, 3.0], name=0, index=ind)
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
df = datetime_frame
result = df.quantile(
    0.1, axis=0, numeric_only=True, interpolation=interpolation, method=method
)
expected = Series(
    [np.percentile(df[col], 10) for col in df.columns],
    index=df.columns,
    name=0.1,
)
if interpolation == "linear":
    # np.percentile values only comparable to linear interpolation
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result.index, expected.index)
    request.node.add_marker(
        pytest.mark.xfail(
            using_array_manager, reason="Name set incorrectly for arraymanager"
        )
    )
    assert result.name == expected.name

result = df.quantile(
    0.9, axis=1, numeric_only=True, interpolation=interpolation, method=method
)
expected = Series(
    [np.percentile(df.loc[date], 90) for date in df.index],
    index=df.index,
    name=0.9,
)
if interpolation == "linear":
    # np.percentile values only comparable to linear interpolation
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result.index, expected.index)
    request.node.add_marker(
        pytest.mark.xfail(
            using_array_manager, reason="Name set incorrectly for arraymanager"
        )
    )
    assert result.name == expected.name

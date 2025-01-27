# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
if left.dtype.name == "json":
    assert left.dtype == right.dtype
    left = pd.Series(
        JSONArray(left.values.astype(object)), index=left.index, name=left.name
    )
    right = pd.Series(
        JSONArray(right.values.astype(object)),
        index=right.index,
        name=right.name,
    )
tm.assert_series_equal(left, right, *args, **kwargs)

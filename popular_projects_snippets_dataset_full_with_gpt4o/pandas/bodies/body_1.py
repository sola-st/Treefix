# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_transform.py
# GH 35964
with np.errstate(all="ignore"):
    expected = concat([np.sqrt(string_series), np.abs(string_series)], axis=1)
expected.columns = ["foo", "bar"]
result = string_series.transform(box({"foo": np.sqrt, "bar": np.abs}))
tm.assert_frame_equal(result, expected)

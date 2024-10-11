# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_convert.py
# GH#6326
obj = frame_or_series(
    np.arange(0, 5),
    index=date_range("20131027", periods=5, freq="1H", tz="Europe/Berlin"),
)
orig = obj.copy()
result = obj.tz_convert("UTC", copy=copy)
expected = frame_or_series(np.arange(0, 5), index=obj.index.tz_convert("UTC"))
tm.assert_equal(result, expected)
tm.assert_equal(obj, orig)
assert result.index is not obj.index
assert result is not obj

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_localize.py
# GH#6326
obj = frame_or_series(
    np.arange(0, 5), index=date_range("20131027", periods=5, freq="1H", tz=None)
)
orig = obj.copy()
result = obj.tz_localize("UTC", copy=copy)
expected = frame_or_series(
    np.arange(0, 5),
    index=date_range("20131027", periods=5, freq="1H", tz="UTC"),
)
tm.assert_equal(result, expected)
tm.assert_equal(obj, orig)
assert result.index is not obj.index
assert result is not obj

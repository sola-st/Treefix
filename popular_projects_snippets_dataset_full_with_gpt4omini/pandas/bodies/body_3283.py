# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#41409
tdi = pd.timedelta_range("1 Day", periods=3)
obj = frame_or_series(tdi)

expected = frame_or_series(["1 days", "2 days", "3 days"], dtype="string")
result = obj.astype("string")
tm.assert_equal(result, expected)

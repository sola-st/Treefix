# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH26683
tz = tz_aware_fixture
idx = date_range("2019-01-01", periods=5, tz=tz)
df = DataFrame({"x": list(range(5))}, index=idx)

expected = df.head(3)
actual = df.reindex(idx[:3], method="nearest")
tm.assert_frame_equal(expected, actual)

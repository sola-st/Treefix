# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#16889
# support .loc with alignment and tz-aware DatetimeIndex
mask = np.array([True, False, True, False])

idx = date_range("20010101", periods=4, tz=tz)
df = DataFrame({"a": np.arange(4)}, index=idx).astype("float64")

result = df.copy()
result.loc[mask, :] = df.loc[mask, :]
tm.assert_frame_equal(result, df)

result = df.copy()
result.loc[mask] = df.loc[mask]
tm.assert_frame_equal(result, df)

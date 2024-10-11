# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#10521 "x" and "z" are both scalar indexing, so those levels are dropped
mi = MultiIndex.from_arrays([["x"], ["y"], ["z"]], names=["a", "b", "c"])
df = DataFrame({"d": [0]}, index=mi)
expected = df.droplevel([0, 2])
result = df.loc["x", :, "z"]
tm.assert_frame_equal(result, expected)

ser = Series([0], index=mi)
result = ser.loc["x", :, "z"]
expected = Series([0], index=Index(["y"], name="b"))
tm.assert_series_equal(result, expected)

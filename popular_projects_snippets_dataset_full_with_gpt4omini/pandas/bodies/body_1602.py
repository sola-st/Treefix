# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH: 26491
obj = frame_or_series(range(4), index=[value, "first", 2, "third"])
result = obj.loc[value:"third"]
expected = frame_or_series(range(4), index=[value, "first", 2, "third"])
tm.assert_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#10692
result = DataFrame({"x": range(10**6)}, dtype="int64")
result.loc[len(result)] = len(result) + 1
expected = DataFrame({"x": range(10**6 + 1)}, dtype="int64")
tm.assert_frame_equal(result, expected)

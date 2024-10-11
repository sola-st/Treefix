# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# https://github.com/pandas-dev/pandas/issues/12392
df = DataFrame({"A": [1, 2], "B": [1, 2]}, index=["X", "Y"])
expected = DataFrame({"a": [1, 2], "b": [1, 2]}, index=["X", "Y"])

result = df.rename(str.lower, axis=1)
tm.assert_frame_equal(result, expected)

result = df.rename(str.lower, axis="columns")
tm.assert_frame_equal(result, expected)

result = df.rename({"A": "a", "B": "b"}, axis=1)
tm.assert_frame_equal(result, expected)

result = df.rename({"A": "a", "B": "b"}, axis="columns")
tm.assert_frame_equal(result, expected)

# Index
expected = DataFrame({"A": [1, 2], "B": [1, 2]}, index=["x", "y"])
result = df.rename(str.lower, axis=0)
tm.assert_frame_equal(result, expected)

result = df.rename(str.lower, axis="index")
tm.assert_frame_equal(result, expected)

result = df.rename({"X": "x", "Y": "y"}, axis=0)
tm.assert_frame_equal(result, expected)

result = df.rename({"X": "x", "Y": "y"}, axis="index")
tm.assert_frame_equal(result, expected)

result = df.rename(mapper=str.lower, axis="index")
tm.assert_frame_equal(result, expected)

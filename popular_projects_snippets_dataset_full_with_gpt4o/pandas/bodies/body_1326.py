# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH10547 and GH10779
# negative integers should be able to reach index 0
df = DataFrame({"A": [2, 3, 5], "B": [7, 11, 13]})
s = df["A"]

expected = df.iloc[0]
result = df.iloc[-3]
tm.assert_series_equal(result, expected)

expected = df.iloc[[0]]
result = df.iloc[[-3]]
tm.assert_frame_equal(result, expected)

expected = s.iloc[0]
result = s.iloc[-3]
assert result == expected

expected = s.iloc[[0]]
result = s.iloc[[-3]]
tm.assert_series_equal(result, expected)

# check the length 1 Series case highlighted in GH10547
expected = Series(["a"], index=["A"])
result = expected.iloc[[-1]]
tm.assert_series_equal(result, expected)

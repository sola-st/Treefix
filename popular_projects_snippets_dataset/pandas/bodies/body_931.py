# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py

# GH6493
# iat/iloc with dups

s = Series(range(5), index=[1, 1, 2, 2, 3], dtype="int64")
result = s.iloc[2]
assert result == 2
result = s.iat[2]
assert result == 2

msg = "index 10 is out of bounds for axis 0 with size 5"
with pytest.raises(IndexError, match=msg):
    s.iat[10]
msg = "index -10 is out of bounds for axis 0 with size 5"
with pytest.raises(IndexError, match=msg):
    s.iat[-10]

result = s.iloc[[2, 3]]
expected = Series([2, 3], [2, 2], dtype="int64")
tm.assert_series_equal(result, expected)

df = s.to_frame()
result = df.iloc[2]
expected = Series(2, index=[0], name=2)
tm.assert_series_equal(result, expected)

result = df.iat[2, 0]
assert result == 2

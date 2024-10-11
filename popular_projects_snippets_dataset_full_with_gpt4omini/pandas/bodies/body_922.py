# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iat.py
# GH#4390, iat incorrectly indexing
index = period_range("1/1/2001", periods=10)
ser = Series(np.random.randn(10), index=index)
expected = ser[index[0]]
result = ser.iat[0]
assert expected == result

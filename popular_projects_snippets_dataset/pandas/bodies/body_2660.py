# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# https://github.com/pandas-dev/pandas/pull/46018
df = tm.SubclassedDataFrame({"A": [0, 1, 2]})
result = df.replace([1, 2], method="ffill")
expected = tm.SubclassedDataFrame({"A": [0, 0, 0]})
assert isinstance(result, tm.SubclassedDataFrame)
tm.assert_frame_equal(result, expected)

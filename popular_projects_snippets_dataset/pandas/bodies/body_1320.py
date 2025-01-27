# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#32085 index with duplicates doesn't matter for _is_scalar_access
index = Index([1, 2, 1])
ser = Series(range(3), index=index)

assert ser.iloc._is_scalar_access((1,))

df = ser.to_frame()
assert df.iloc._is_scalar_access((1, 0))

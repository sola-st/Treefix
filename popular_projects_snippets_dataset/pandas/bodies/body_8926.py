# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# GH#27910
arr = SparseArray([0, 1], fill_value=0)
df = pd.DataFrame([[1, 2], [3, 4]])
result = arr.__add__(df)
assert result is NotImplemented

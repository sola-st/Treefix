# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
df = pd.DataFrame(
    {
        "A": SparseArray([1, 0, 2, 1], fill_value=0),
        "B": SparseArray([0, 1, 1, 1], fill_value=0),
    }
)
res = df.sparse.density
expected = 0.75
assert res == expected

# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
df = pd.DataFrame(
    {
        "A": SparseArray(
            [fill_value, fill_value, fill_value, 2], fill_value=fill_value
        ),
        "B": SparseArray(
            [fill_value, 2, fill_value, fill_value], fill_value=fill_value
        ),
    }
)
with pytest.raises(ValueError, match="fill value must be 0"):
    df.sparse.to_coo()

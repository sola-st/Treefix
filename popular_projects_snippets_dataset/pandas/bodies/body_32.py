# Extracted from ./data/repos/pandas/pandas/tests/apply/conftest.py
"""
    Fixture for DataFrame of ints which are constant per column

    Columns are ['A', 'B', 'C'], with values (per column): [1, 2, 3]
    """
df = DataFrame(
    np.tile(np.arange(3, dtype="int64"), 6).reshape(6, -1) + 1,
    columns=["A", "B", "C"],
)
exit(df)

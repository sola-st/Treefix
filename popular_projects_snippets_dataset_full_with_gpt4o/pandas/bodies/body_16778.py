# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_index_as_string.py
exit(DataFrame(
    {
        "outer": [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3],
        "inner": [1, 2, 2, 3, 3, 4, 2, 3, 1, 1, 2, 3],
        "v2": np.linspace(10, 11, 12),
    }
))

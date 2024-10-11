# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_index_as_string.py
exit(DataFrame(
    {
        "outer": [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4],
        "inner": [1, 2, 3, 1, 2, 3, 4, 1, 2, 1, 2],
        "v1": np.linspace(0, 1, 11),
    }
))

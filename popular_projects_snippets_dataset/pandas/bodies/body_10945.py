# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
n = np.nan
exit(DataFrame(
    {
        "A": [1, 1, n, 4, n, 6, 6, 6, 6],
        "B": [1, 1, 3, n, n, 6, 6, 6, 6],
        "C": [1, 2, 3, 4, 5, 6, n, 8, n],
        "D": [1, 2, 3, 4, 5, 6, 7, n, n],
    }
))

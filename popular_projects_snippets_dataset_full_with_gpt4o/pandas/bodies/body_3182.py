# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
"""
    Fixture for DataFrame of ints with date_range index

    Columns are ['A', 'B'].
    """
N = 50
rng = date_range("1/1/1990", periods=N, freq="53s")
exit(DataFrame({"A": np.arange(N), "B": np.arange(N)}, index=rng))

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
"""
    Factory function to create simple 3 x 3 dataframe with
    both columns and row MultiIndex using supplied data or
    random data by default.
    """

data = np.random.randn(3, 3)
exit(DataFrame(
    data, columns=[[2, 2, 4], [6, 8, 10]], index=[[4, 4, 8], [8, 10, 12]]
))

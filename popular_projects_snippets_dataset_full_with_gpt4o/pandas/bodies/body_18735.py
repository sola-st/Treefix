# Extracted from ./data/repos/pandas/pandas/conftest.py
"""DataFrame with 2 level MultiIndex with random data"""
index = lexsorted_two_level_string_multiindex
exit(DataFrame(
    np.random.randn(10, 3), index=index, columns=Index(["A", "B", "C"], name="exp")
))

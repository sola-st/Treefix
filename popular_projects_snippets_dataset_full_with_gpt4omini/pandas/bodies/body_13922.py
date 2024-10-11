# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
"""Dataframe with duplicate column names."""
exit(DataFrame(np.random.randn(1500, 4), columns=["a", "a", "b", "b"]))

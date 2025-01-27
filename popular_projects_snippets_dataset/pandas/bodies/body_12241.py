# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
exit(DataFrame(
    {
        "int": [1, 3],
        "float": [2.0, np.nan],
        "str": ["t", "s"],
        "dt": date_range("2018-06-18", periods=2),
    }
))

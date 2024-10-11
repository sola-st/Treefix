# Extracted from ./data/repos/pandas/pandas/tests/generic/test_to_xarray.py
exit(DataFrame(
    {
        "a": list("abc"),
        "b": list(range(1, 4)),
        "c": np.arange(3, 6).astype("u1"),
        "d": np.arange(4.0, 7.0, dtype="float64"),
        "e": [True, False, True],
        "f": Categorical(list("abc")),
        "g": date_range("20130101", periods=3),
        "h": date_range("20130101", periods=3, tz="US/Eastern"),
    }
))

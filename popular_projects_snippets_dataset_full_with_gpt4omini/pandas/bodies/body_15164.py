# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
series = Series([0, 1000, 2000, pd.NaT.value], dtype="M8[ns]")

result = repr(series)
expected = (
    "0   1970-01-01 00:00:00.000000\n"
    "1   1970-01-01 00:00:00.000001\n"
    "2   1970-01-01 00:00:00.000002\n"
    "3                          NaT\n"
    "dtype: datetime64[ns]"
)
assert result == expected

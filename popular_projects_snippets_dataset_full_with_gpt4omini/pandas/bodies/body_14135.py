# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 12615
index = pd.period_range("2013-01", periods=6, freq="M")
s = Series(np.arange(6, dtype="int64"), index=index)
exp = (
    "2013-01    0\n"
    "2013-02    1\n"
    "2013-03    2\n"
    "2013-04    3\n"
    "2013-05    4\n"
    "2013-06    5\n"
    "Freq: M, dtype: int64"
)
assert str(s) == exp

s = Series(index)
exp = (
    "0    2013-01\n"
    "1    2013-02\n"
    "2    2013-03\n"
    "3    2013-04\n"
    "4    2013-05\n"
    "5    2013-06\n"
    "dtype: period[M]"
)
assert str(s) == exp

# periods with mixed freq
s = Series(
    [
        pd.Period("2011-01", freq="M"),
        pd.Period("2011-02-01", freq="D"),
        pd.Period("2011-03-01 09:00", freq="H"),
    ]
)
exp = (
    "0             2011-01\n1          2011-02-01\n"
    "2    2011-03-01 09:00\ndtype: object"
)
assert str(s) == exp

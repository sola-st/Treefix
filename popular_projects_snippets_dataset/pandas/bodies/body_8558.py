# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# see gh-11488
result = Index(
    [pd.NaT, Timestamp("2011-01-01"), pd.NaT, Timestamp("2011-01-02")],
    name="idx",
)
exp = DatetimeIndex(
    [pd.NaT, Timestamp("2011-01-01"), pd.NaT, Timestamp("2011-01-02")],
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is None

# Same tz results in DatetimeIndex
result = Index(
    [
        pd.NaT,
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        pd.NaT,
        Timestamp("2011-01-02 10:00", tz="Asia/Tokyo"),
    ],
    name="idx",
)
exp = DatetimeIndex(
    [
        pd.NaT,
        Timestamp("2011-01-01 10:00"),
        pd.NaT,
        Timestamp("2011-01-02 10:00"),
    ],
    tz="Asia/Tokyo",
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is not None
assert result.tz == exp.tz

# same tz results in DatetimeIndex (DST)
result = Index(
    [
        Timestamp("2011-01-01 10:00", tz="US/Eastern"),
        pd.NaT,
        Timestamp("2011-08-01 10:00", tz="US/Eastern"),
    ],
    name="idx",
)
exp = DatetimeIndex(
    [Timestamp("2011-01-01 10:00"), pd.NaT, Timestamp("2011-08-01 10:00")],
    tz="US/Eastern",
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is not None
assert result.tz == exp.tz

# different tz results in Index(dtype=object)
result = Index(
    [
        pd.NaT,
        Timestamp("2011-01-01 10:00"),
        pd.NaT,
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    name="idx",
)
exp = Index(
    [
        pd.NaT,
        Timestamp("2011-01-01 10:00"),
        pd.NaT,
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    dtype="object",
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert not isinstance(result, DatetimeIndex)

result = Index(
    [
        pd.NaT,
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        pd.NaT,
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    name="idx",
)
exp = Index(
    [
        pd.NaT,
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        pd.NaT,
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    dtype="object",
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert not isinstance(result, DatetimeIndex)

# all NaT
result = Index([pd.NaT, pd.NaT], name="idx")
exp = DatetimeIndex([pd.NaT, pd.NaT], name="idx")
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is None

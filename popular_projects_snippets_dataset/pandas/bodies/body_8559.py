# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 11488 (not changed, added explicit tests)

# no tz results in DatetimeIndex
result = DatetimeIndex(
    [Timestamp("2011-01-01"), Timestamp("2011-01-02")], name="idx"
)
exp = DatetimeIndex(
    [Timestamp("2011-01-01"), Timestamp("2011-01-02")], name="idx"
)
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)

# same tz results in DatetimeIndex
result = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        Timestamp("2011-01-02 10:00", tz="Asia/Tokyo"),
    ],
    name="idx",
)
exp = DatetimeIndex(
    [Timestamp("2011-01-01 10:00"), Timestamp("2011-01-02 10:00")],
    tz="Asia/Tokyo",
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)

# same tz results in DatetimeIndex (DST)
result = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00", tz="US/Eastern"),
        Timestamp("2011-08-01 10:00", tz="US/Eastern"),
    ],
    name="idx",
)
exp = DatetimeIndex(
    [Timestamp("2011-01-01 10:00"), Timestamp("2011-08-01 10:00")],
    tz="US/Eastern",
    name="idx",
)
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)

# tz mismatch affecting to tz-aware raises TypeError/ValueError

msg = "cannot be converted to datetime64"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(
        [
            Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
            Timestamp("2011-01-02 10:00", tz="US/Eastern"),
        ],
        name="idx",
    )

# pre-2.0 this raised bc of awareness mismatch. in 2.0 with a tz#
#  specified we behave as if this was called pointwise, so
#  the naive Timestamp is treated as a wall time.
dti = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00"),
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    tz="Asia/Tokyo",
    name="idx",
)
expected = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        Timestamp("2011-01-02 10:00", tz="US/Eastern").tz_convert("Asia/Tokyo"),
    ],
    tz="Asia/Tokyo",
    name="idx",
)
tm.assert_index_equal(dti, expected)

# pre-2.0 mixed-tz scalars raised even if a tz/dtype was specified.
#  as of 2.0 we successfully return the requested tz/dtype
dti = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    tz="US/Eastern",
    name="idx",
)
expected = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo").tz_convert("US/Eastern"),
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    tz="US/Eastern",
    name="idx",
)
tm.assert_index_equal(dti, expected)

# same thing but pass dtype instead of tz
dti = DatetimeIndex(
    [
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        Timestamp("2011-01-02 10:00", tz="US/Eastern"),
    ],
    dtype="M8[ns, US/Eastern]",
    name="idx",
)
tm.assert_index_equal(dti, expected)

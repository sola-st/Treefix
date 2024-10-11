# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# See GH#14068
# preliminary test scalar analogue of vectorized tests below
# TODO: Make raised error message more informative and test
with pytest.raises(OutOfBoundsDatetime, match="10155196800000000000"):
    pd.to_timedelta(106580, "D") + Timestamp("2000")
with pytest.raises(OutOfBoundsDatetime, match="10155196800000000000"):
    Timestamp("2000") + pd.to_timedelta(106580, "D")

_NaT = NaT.value + 1
msg = "Overflow in int64 addition"
with pytest.raises(OverflowError, match=msg):
    pd.to_timedelta([106580], "D") + Timestamp("2000")
with pytest.raises(OverflowError, match=msg):
    Timestamp("2000") + pd.to_timedelta([106580], "D")
with pytest.raises(OverflowError, match=msg):
    pd.to_timedelta([_NaT]) - Timedelta("1 days")
with pytest.raises(OverflowError, match=msg):
    pd.to_timedelta(["5 days", _NaT]) - Timedelta("1 days")
with pytest.raises(OverflowError, match=msg):
    (
        pd.to_timedelta([_NaT, "5 days", "1 hours"])
        - pd.to_timedelta(["7 seconds", _NaT, "4 hours"])
    )

# These should not overflow!
exp = TimedeltaIndex([NaT])
result = pd.to_timedelta([NaT]) - Timedelta("1 days")
tm.assert_index_equal(result, exp)

exp = TimedeltaIndex(["4 days", NaT])
result = pd.to_timedelta(["5 days", NaT]) - Timedelta("1 days")
tm.assert_index_equal(result, exp)

exp = TimedeltaIndex([NaT, NaT, "5 hours"])
result = pd.to_timedelta([NaT, "5 days", "1 hours"]) + pd.to_timedelta(
    ["7 seconds", NaT, "4 hours"]
)
tm.assert_index_equal(result, exp)

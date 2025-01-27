# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
t1 = timedelta_range("1 days", periods=3, freq="1 min 2 s 3 us")
t2 = -1 * t1
t1a = timedelta_range("1 days", periods=3, freq="1 min 2 s")
t1c = TimedeltaIndex([1, 1, 1], unit="D")

# note that negative times round DOWN! so don't give whole numbers
for (freq, s1, s2) in [
    ("N", t1, t2),
    ("U", t1, t2),
    (
        "L",
        t1a,
        TimedeltaIndex(
            ["-1 days +00:00:00", "-2 days +23:58:58", "-2 days +23:57:56"]
        ),
    ),
    (
        "S",
        t1a,
        TimedeltaIndex(
            ["-1 days +00:00:00", "-2 days +23:58:58", "-2 days +23:57:56"]
        ),
    ),
    ("12T", t1c, TimedeltaIndex(["-1 days", "-1 days", "-1 days"])),
    ("H", t1c, TimedeltaIndex(["-1 days", "-1 days", "-1 days"])),
    ("d", t1c, TimedeltaIndex([-1, -1, -1], unit="D")),
]:

    r1 = t1.round(freq)
    tm.assert_index_equal(r1, s1)
    r2 = t2.round(freq)
    tm.assert_index_equal(r2, s2)

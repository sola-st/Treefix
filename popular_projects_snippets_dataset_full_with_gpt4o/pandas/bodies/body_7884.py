# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_setops.py
# union
other1 = period_range("1/1/2000", freq="D", periods=5)
rng1 = period_range("1/6/2000", freq="D", periods=5)
expected1 = PeriodIndex(
    [
        "2000-01-06",
        "2000-01-07",
        "2000-01-08",
        "2000-01-09",
        "2000-01-10",
        "2000-01-01",
        "2000-01-02",
        "2000-01-03",
        "2000-01-04",
        "2000-01-05",
    ],
    freq="D",
)

rng2 = period_range("1/1/2000", freq="D", periods=5)
other2 = period_range("1/4/2000", freq="D", periods=5)
expected2 = period_range("1/1/2000", freq="D", periods=8)

rng3 = period_range("1/1/2000", freq="D", periods=5)
other3 = PeriodIndex([], freq="D")
expected3 = period_range("1/1/2000", freq="D", periods=5)

rng4 = period_range("2000-01-01 09:00", freq="H", periods=5)
other4 = period_range("2000-01-02 09:00", freq="H", periods=5)
expected4 = PeriodIndex(
    [
        "2000-01-01 09:00",
        "2000-01-01 10:00",
        "2000-01-01 11:00",
        "2000-01-01 12:00",
        "2000-01-01 13:00",
        "2000-01-02 09:00",
        "2000-01-02 10:00",
        "2000-01-02 11:00",
        "2000-01-02 12:00",
        "2000-01-02 13:00",
    ],
    freq="H",
)

rng5 = PeriodIndex(
    ["2000-01-01 09:01", "2000-01-01 09:03", "2000-01-01 09:05"], freq="T"
)
other5 = PeriodIndex(
    ["2000-01-01 09:01", "2000-01-01 09:05", "2000-01-01 09:08"], freq="T"
)
expected5 = PeriodIndex(
    [
        "2000-01-01 09:01",
        "2000-01-01 09:03",
        "2000-01-01 09:05",
        "2000-01-01 09:08",
    ],
    freq="T",
)

rng6 = period_range("2000-01-01", freq="M", periods=7)
other6 = period_range("2000-04-01", freq="M", periods=7)
expected6 = period_range("2000-01-01", freq="M", periods=10)

rng7 = period_range("2003-01-01", freq="A", periods=5)
other7 = period_range("1998-01-01", freq="A", periods=8)
expected7 = PeriodIndex(
    [
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "1998",
        "1999",
        "2000",
        "2001",
        "2002",
    ],
    freq="A",
)

rng8 = PeriodIndex(
    ["1/3/2000", "1/2/2000", "1/1/2000", "1/5/2000", "1/4/2000"], freq="D"
)
other8 = period_range("1/6/2000", freq="D", periods=5)
expected8 = PeriodIndex(
    [
        "1/3/2000",
        "1/2/2000",
        "1/1/2000",
        "1/5/2000",
        "1/4/2000",
        "1/6/2000",
        "1/7/2000",
        "1/8/2000",
        "1/9/2000",
        "1/10/2000",
    ],
    freq="D",
)

for rng, other, expected in [
    (rng1, other1, expected1),
    (rng2, other2, expected2),
    (rng3, other3, expected3),
    (rng4, other4, expected4),
    (rng5, other5, expected5),
    (rng6, other6, expected6),
    (rng7, other7, expected7),
    (rng8, other8, expected8),
]:

    result_union = rng.union(other, sort=sort)
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result_union, expected)

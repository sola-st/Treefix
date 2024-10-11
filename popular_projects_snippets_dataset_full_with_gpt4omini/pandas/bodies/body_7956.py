# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
idx = period_range(
    start=Period(ordinal=1, freq="N"), end=Period(ordinal=4, freq="N"), freq="N"
)
exp = PeriodIndex(
    [
        Period(ordinal=1, freq="N"),
        Period(ordinal=2, freq="N"),
        Period(ordinal=3, freq="N"),
        Period(ordinal=4, freq="N"),
    ],
    freq="N",
)
tm.assert_index_equal(idx, exp)

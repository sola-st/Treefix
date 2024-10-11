# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_setops.py
# GH#36289
idx = period_range("2011-01-01", periods=2)
idx_dup = idx.append(idx)

idx2 = period_range("2011-01-02", periods=2)
idx2_dup = idx2.append(idx2)
result = idx_dup.union(idx2_dup)

expected = PeriodIndex(
    [
        "2011-01-01",
        "2011-01-01",
        "2011-01-02",
        "2011-01-02",
        "2011-01-03",
        "2011-01-03",
    ],
    freq="D",
)
tm.assert_index_equal(result, expected)

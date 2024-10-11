# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
idx = Index(
    [np.nan, Interval(0, 1, closed=closed), Interval(1, 2, closed=closed)]
)
idx2 = IntervalIndex.from_arrays([np.nan, 0, 1], [np.nan, 1, 2], closed=closed)
assert idx.equals(idx2)

msg = (
    "missing values must be missing in the same location both left "
    "and right sides"
)
with pytest.raises(ValueError, match=msg):
    IntervalIndex.from_arrays(
        [np.nan, 0, 1], np.array([0, 1, 2]), closed=closed
    )

tm.assert_numpy_array_equal(isna(idx), np.array([True, False, False]))

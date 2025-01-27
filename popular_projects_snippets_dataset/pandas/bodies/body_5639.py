# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 13663
s = Series(
    [
        datetime(3000, 1, 1),
        datetime(5000, 1, 1),
        datetime(5000, 1, 1),
        datetime(6000, 1, 1),
        datetime(3000, 1, 1),
        datetime(3000, 1, 1),
    ]
)
res = s.value_counts()

exp_index = Index(
    [datetime(3000, 1, 1), datetime(5000, 1, 1), datetime(6000, 1, 1)],
    dtype=object,
)
exp = Series([3, 2, 1], index=exp_index)
tm.assert_series_equal(res, exp)

# GH 12424
with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    res = to_datetime(Series(["2362-01-01", np.nan]), errors="ignore")
exp = Series(["2362-01-01", np.nan], dtype=object)
tm.assert_series_equal(res, exp)

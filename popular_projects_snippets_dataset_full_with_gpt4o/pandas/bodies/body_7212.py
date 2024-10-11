# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
# GH#49660 pre-2.0 Index.astype from floating to M8/m8/Period raised,
#  inconsistent with Series.astype
idx = Index([0, 1.1, 2], dtype=np.float64)

result = idx.astype(dtype)
if dtype[0] == "M":
    expected = to_datetime(idx.values)
else:
    expected = to_timedelta(idx.values)
tm.assert_index_equal(result, expected)

# check that we match Series behavior
result = idx.to_series().set_axis(range(3)).astype(dtype)
expected = expected.to_series().set_axis(range(3))
tm.assert_series_equal(result, expected)

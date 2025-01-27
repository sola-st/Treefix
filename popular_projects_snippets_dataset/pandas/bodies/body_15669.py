# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
idx = MultiIndex.from_tuples([(0, "a"), (1, "b"), (2, "c")])
s = Series([1, 2, np.nan], index=idx)

expected = s.copy()
expected.loc[2] = 2
result = s.interpolate()
tm.assert_series_equal(result, expected)

msg = "Only `method=linear` interpolation is supported on MultiIndexes"
if check_scipy:
    with pytest.raises(ValueError, match=msg):
        s.interpolate(method="polynomial", order=1)

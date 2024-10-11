# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
series = tm.makeTimeSeries().rename("ts")
other = func(series)
results = divmod(series, other)
if isinstance(other, abc.Iterable) and len(series) != len(other):
    # if the lengths don't match, this is the test where we use
    # `tser[::2]`. Pad every other value in `other_np` with nan.
    other_np = []
    for n in other:
        other_np.append(n)
        other_np.append(np.nan)
else:
    other_np = other
other_np = np.asarray(other_np)
with np.errstate(all="ignore"):
    expecteds = divmod(series.values, np.asarray(other_np))

for result, expected in zip(results, expecteds):
    # check the values, name, and index separately
    tm.assert_almost_equal(np.asarray(result), expected)

    assert result.name == series.name
    tm.assert_index_equal(result.index, series.index._with_freq(None))

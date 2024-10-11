# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
index = simple_index
expected = index + index.freq

# don't compare the freqs
if isinstance(expected, (pd.DatetimeIndex, pd.TimedeltaIndex)):
    expected = expected._with_freq(None)

result = index.map(mapper(expected, index))
tm.assert_index_equal(result, expected)

expected = pd.Index([pd.NaT] + index[1:].tolist())
result = index.map(mapper(expected, index))
tm.assert_index_equal(result, expected)

# empty map; these map to np.nan because we cannot know
# to re-infer things
expected = pd.Index([np.nan] * len(index))
result = index.map(mapper([], []))
tm.assert_index_equal(result, expected)

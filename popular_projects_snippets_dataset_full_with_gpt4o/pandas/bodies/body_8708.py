# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
expected = arr1d.copy()[::-1]
if not isinstance(expected, PeriodArray):
    expected = expected._with_freq(None)

cat = pd.Categorical(arr1d)
if as_index:
    cat = pd.CategoricalIndex(cat)

arr1d[:] = cat[::-1]

tm.assert_equal(arr1d, expected)

# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py

expected = arr1d.copy()[::-1]
if expected.dtype.kind in ["m", "M"]:
    expected = expected._with_freq(None)

vals = expected
if box is list:
    vals = list(vals)
elif box is np.array:
    # if we do np.array(x).astype(object) then dt64 and td64 cast to ints
    vals = np.array(vals.astype(object))
elif box is PandasArray:
    vals = box(np.asarray(vals, dtype=object))
else:
    vals = box(vals).astype(object)

arr1d[:] = vals

tm.assert_equal(arr1d, expected)

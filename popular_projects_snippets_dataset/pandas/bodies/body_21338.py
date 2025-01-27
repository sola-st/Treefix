# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
dtypes = {str(x.dtype) for x in to_concat}
if len(dtypes) != 1:
    raise ValueError("to_concat must have the same dtype (tz)", dtypes)

new_values = [x._ndarray for x in to_concat]
new_arr = np.concatenate(new_values, axis=axis)
exit(to_concat[0]._from_backing_data(new_arr))

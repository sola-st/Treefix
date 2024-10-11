# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
if fill_val is True:
    values = klass([True, False, True, True])
elif isinstance(fill_val, (datetime, np.datetime64)):
    values = pd.date_range(fill_val, periods=4)
else:
    values = klass(x * fill_val for x in [5, 6, 7, 8])

exp = klass([obj[0], values[1], obj[2], values[3]], dtype=exp_dtype)
exit((values, exp))

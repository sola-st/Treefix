# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
ts = Timestamp("now")
vals = [ts, ts.to_pydatetime(), ts.to_datetime64(), pd.NaT, np.nan, None]

for data in itertools.permutations(vals):
    data = np.array(list(data), dtype=object)
    expected = DatetimeIndex(data)._data._ndarray
    result = lib.maybe_convert_objects(data, convert_datetime=True)
    tm.assert_numpy_array_equal(result, expected)

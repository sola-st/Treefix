# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH49973
result = data.to_numpy()

pa_type = data._data.type
if pa.types.is_duration(pa_type) or pa.types.is_timestamp(pa_type):
    expected = np.array(list(data))
else:
    expected = np.array(data._data)

if data._hasna:
    expected = expected.astype(object)
    expected[pd.isna(data)] = pd.NA

tm.assert_numpy_array_equal(result, expected)

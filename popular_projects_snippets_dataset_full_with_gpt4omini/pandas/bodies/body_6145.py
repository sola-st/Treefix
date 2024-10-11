# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH 33172
data = data[:10].unique()
values = np.array(data[~data.isna()])
ser = pd.Series(data, dtype=data.dtype)

result = ser.value_counts(normalize=True).sort_index()

if not isinstance(data, pd.Categorical):
    expected = pd.Series([1 / len(values)] * len(values), index=result.index)
else:
    expected = pd.Series(0.0, index=result.index)
    expected[result > 0] = 1 / len(values)
if na_value_for_dtype(data.dtype) is pd.NA:
    # TODO(GH#44692): avoid special-casing
    expected = expected.astype("Float64")

self.assert_series_equal(result, expected)

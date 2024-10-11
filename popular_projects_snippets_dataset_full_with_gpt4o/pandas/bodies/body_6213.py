# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
fill_value = data_missing[1]

if fillna_method == "ffill":
    data_missing = data_missing[::-1]

result = pd.Series(data_missing).fillna(method=fillna_method)
expected = pd.Series(
    data_missing._from_sequence(
        [fill_value, fill_value], dtype=data_missing.dtype
    )
)

self.assert_series_equal(result, expected)

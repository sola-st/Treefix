# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_value_counts.py
df_no_cols = pd.DataFrame()

result = df_no_cols.value_counts(normalize=True)
expected = pd.Series([], dtype=np.float64, index=np.array([], dtype=np.intp))

tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# GH-28287
arr = SparseArray([np.nan, 1], fill_value=fill_value)
exp = SparseArray([1.0], fill_value=fill_value)
tm.assert_sp_array_equal(arr.dropna(), exp)

df = pd.DataFrame({"a": [0, 1], "b": arr})
expected_df = pd.DataFrame({"a": [1], "b": exp}, index=pd.Index([1]))
tm.assert_equal(df.dropna(), expected_df)

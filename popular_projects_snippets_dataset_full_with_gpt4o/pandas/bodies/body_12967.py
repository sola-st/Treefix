# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH#35211
basename = "df_mangle_dup_col_dtypes"
dtype_dict = {"a": str, **dtypes}
dtype_dict_copy = dtype_dict.copy()
# GH#42462
result = pd.read_excel(basename + read_ext, dtype=dtype_dict)
expected = DataFrame({"a": ["1"], "a.1": [exp_value]})
assert dtype_dict == dtype_dict_copy, "dtype dict changed"
tm.assert_frame_equal(result, expected)

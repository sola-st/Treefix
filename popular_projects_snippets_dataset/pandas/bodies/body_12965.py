# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH#36712
if read_ext in (".xlsb", ".xls"):
    pytest.skip(f"No engine for filetype: '{read_ext}'")

df = DataFrame({"a": [np.nan, 1.0], "b": [2.5, np.nan]})
with tm.ensure_clean(read_ext) as file_path:
    df.to_excel(file_path, "test", index=False)
    result = pd.read_excel(
        file_path, sheet_name="test", use_nullable_dtypes=True, dtype="float64"
    )
tm.assert_frame_equal(result, df)

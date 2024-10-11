# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH#36712
if read_ext in (".xlsb", ".xls"):
    pytest.skip(f"No engine for filetype: '{read_ext}'")

df = DataFrame(
    {
        "a": Series([1, 3], dtype="Int64"),
        "b": Series([2.5, 4.5], dtype="Float64"),
        "c": Series([True, False], dtype="boolean"),
        "d": Series(["a", "b"], dtype="string"),
        "e": Series([pd.NA, 6], dtype="Int64"),
        "f": Series([pd.NA, 7.5], dtype="Float64"),
        "g": Series([pd.NA, True], dtype="boolean"),
        "h": Series([pd.NA, "a"], dtype="string"),
        "i": Series([pd.Timestamp("2019-12-31")] * 2),
        "j": Series([pd.NA, pd.NA], dtype="Int64"),
    }
)
with tm.ensure_clean(read_ext) as file_path:
    df.to_excel(file_path, "test", index=False)
    with pd.option_context("mode.dtype_backend", dtype_backend):
        result = pd.read_excel(
            file_path, sheet_name="test", use_nullable_dtypes=True
        )
if dtype_backend == "pyarrow":
    import pyarrow as pa

    from pandas.arrays import ArrowExtensionArray

    expected = DataFrame(
        {
            col: ArrowExtensionArray(pa.array(df[col], from_pandas=True))
            for col in df.columns
        }
    )
    # pyarrow by default infers timestamp resolution as us, not ns
    expected["i"] = ArrowExtensionArray(
        expected["i"].array._data.cast(pa.timestamp(unit="us"))
    )
    # pyarrow supports a null type, so don't have to default to Int64
    expected["j"] = ArrowExtensionArray(pa.array([None, None]))
else:
    expected = df
tm.assert_frame_equal(result, expected)

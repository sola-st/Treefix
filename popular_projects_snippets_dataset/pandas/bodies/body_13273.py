# Extracted from ./data/repos/pandas/pandas/tests/io/test_orc.py
df = pd.DataFrame(
    {
        "string": list("abc"),
        "string_with_nan": ["a", np.nan, "c"],
        "string_with_none": ["a", None, "c"],
        "bytes": [b"foo", b"bar", None],
        "int": list(range(1, 4)),
        "float": np.arange(4.0, 7.0, dtype="float64"),
        "float_with_nan": [2.0, np.nan, 3.0],
        "bool": [True, False, True],
        "bool_with_na": [True, False, None],
        "datetime": pd.date_range("20130101", periods=3),
        "datetime_with_nat": [
            pd.Timestamp("20130101"),
            pd.NaT,
            pd.Timestamp("20130103"),
        ],
    }
)

bytes_data = df.copy().to_orc()
with pd.option_context("mode.dtype_backend", "pyarrow"):
    result = read_orc(BytesIO(bytes_data), use_nullable_dtypes=True)

expected = pd.DataFrame(
    {
        col: pd.arrays.ArrowExtensionArray(pa.array(df[col], from_pandas=True))
        for col in df.columns
    }
)

tm.assert_frame_equal(result, expected)

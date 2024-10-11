# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH#50750
pa = pytest.importorskip("pyarrow")
ser = Series([1, np.nan, 3], dtype="Int64")

out = ser.to_json(orient=orient)
with pd.option_context("mode.string_storage", string_storage):
    with pd.option_context("mode.dtype_backend", dtype_backend):
        result = read_json(
            out, use_nullable_dtypes=True, orient=orient, typ="series"
        )

expected = Series([1, np.nan, 3], dtype="Int64")

if dtype_backend == "pyarrow":
    from pandas.arrays import ArrowExtensionArray

    expected = Series(ArrowExtensionArray(pa.array(expected, from_pandas=True)))

tm.assert_series_equal(result, expected)

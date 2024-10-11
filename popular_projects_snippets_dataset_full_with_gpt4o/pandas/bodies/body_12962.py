# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 8212
basename = "testdtype"
actual = pd.read_excel(basename + read_ext)

expected = DataFrame(
    {
        "a": [1, 2, 3, 4],
        "b": [2.5, 3.5, 4.5, 5.5],
        "c": [1, 2, 3, 4],
        "d": [1.0, 2.0, np.nan, 4.0],
    }
).reindex(columns=["a", "b", "c", "d"])

tm.assert_frame_equal(actual, expected)

actual = pd.read_excel(
    basename + read_ext, dtype={"a": "float64", "b": "float32", "c": str}
)

expected["a"] = expected["a"].astype("float64")
expected["b"] = expected["b"].astype("float32")
expected["c"] = ["001", "002", "003", "004"]
tm.assert_frame_equal(actual, expected)

msg = "Unable to convert column d to type int64"
with pytest.raises(ValueError, match=msg):
    pd.read_excel(basename + read_ext, dtype={"d": "int64"})

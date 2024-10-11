# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
import pyarrow.parquet as pq

if engine == "fastparquet":
    # We are manually disabling fastparquet's
    # nullable dtype support pending discussion
    mark = pytest.mark.xfail(
        reason="Fastparquet nullable dtype support is disabled"
    )
    request.node.add_marker(mark)

table = pyarrow.table(
    {
        "a": pyarrow.array([1, 2, 3, None], "int64"),
        "b": pyarrow.array([1, 2, 3, None], "uint8"),
        "c": pyarrow.array(["a", "b", "c", None]),
        "d": pyarrow.array([True, False, True, None]),
        # Test that nullable dtypes used even in absence of nulls
        "e": pyarrow.array([1, 2, 3, 4], "int64"),
        # GH 45694
        "f": pyarrow.array([1.0, 2.0, 3.0, None], "float32"),
        "g": pyarrow.array([1.0, 2.0, 3.0, None], "float64"),
    }
)
with tm.ensure_clean() as path:
    # write manually with pyarrow to write integers
    pq.write_table(table, path)
    result1 = read_parquet(path, engine=engine)
    result2 = read_parquet(path, engine=engine, use_nullable_dtypes=True)

assert result1["a"].dtype == np.dtype("float64")
expected = pd.DataFrame(
    {
        "a": pd.array([1, 2, 3, None], dtype="Int64"),
        "b": pd.array([1, 2, 3, None], dtype="UInt8"),
        "c": pd.array(["a", "b", "c", None], dtype="string"),
        "d": pd.array([True, False, True, None], dtype="boolean"),
        "e": pd.array([1, 2, 3, 4], dtype="Int64"),
        "f": pd.array([1.0, 2.0, 3.0, None], dtype="Float32"),
        "g": pd.array([1.0, 2.0, 3.0, None], dtype="Float64"),
    }
)
if engine == "fastparquet":
    # Fastparquet doesn't support string columns yet
    # Only int and boolean
    result2 = result2.drop("c", axis=1)
    expected = expected.drop("c", axis=1)
tm.assert_frame_equal(result2, expected)

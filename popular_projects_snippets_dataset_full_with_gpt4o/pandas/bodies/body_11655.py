# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#36712
pa = pytest.importorskip("pyarrow")
parser = all_parsers
engine = parser.engine

data = """a,b,c,d,e,f,g,h,i,j
1,2.5,True,a,,,,,12-31-2019,
3,4.5,False,b,6,7.5,True,a,12-31-2019,
"""
with pd.option_context("mode.dtype_backend", "pyarrow"):
    if engine == "c":
        request.node.add_marker(
            pytest.mark.xfail(
                raises=NotImplementedError,
                reason=f"Not implemented with engine={parser.engine}",
            )
        )
    result = parser.read_csv(
        StringIO(data), use_nullable_dtypes=True, parse_dates=["i"]
    )
    expected = DataFrame(
        {
            "a": pd.Series([1, 3], dtype="int64[pyarrow]"),
            "b": pd.Series([2.5, 4.5], dtype="float64[pyarrow]"),
            "c": pd.Series([True, False], dtype="bool[pyarrow]"),
            "d": pd.Series(["a", "b"], dtype=pd.ArrowDtype(pa.string())),
            "e": pd.Series([pd.NA, 6], dtype="int64[pyarrow]"),
            "f": pd.Series([pd.NA, 7.5], dtype="float64[pyarrow]"),
            "g": pd.Series([pd.NA, True], dtype="bool[pyarrow]"),
            "h": pd.Series(
                [pd.NA if engine == "python" else "", "a"],
                dtype=pd.ArrowDtype(pa.string()),
            ),
            "i": pd.Series([Timestamp("2019-12-31")] * 2),
            "j": pd.Series([pd.NA, pd.NA], dtype="null[pyarrow]"),
        }
    )
tm.assert_frame_equal(result, expected)

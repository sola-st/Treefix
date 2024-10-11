# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#36712

parser = all_parsers

data = """a,b,c,d,e,f,g,h,i,j
1,2.5,True,a,,,,,12-31-2019,
3,4.5,False,b,6,7.5,True,a,12-31-2019,
"""
result = parser.read_csv(
    StringIO(data), use_nullable_dtypes=True, parse_dates=["i"]
)
expected = DataFrame(
    {
        "a": pd.Series([1, 3], dtype="Int64"),
        "b": pd.Series([2.5, 4.5], dtype="Float64"),
        "c": pd.Series([True, False], dtype="boolean"),
        "d": pd.Series(["a", "b"], dtype="string"),
        "e": pd.Series([pd.NA, 6], dtype="Int64"),
        "f": pd.Series([pd.NA, 7.5], dtype="Float64"),
        "g": pd.Series([pd.NA, True], dtype="boolean"),
        "h": pd.Series([pd.NA, "a"], dtype="string"),
        "i": pd.Series([Timestamp("2019-12-31")] * 2),
        "j": pd.Series([pd.NA, pd.NA], dtype="Int64"),
    }
)
tm.assert_frame_equal(result, expected)

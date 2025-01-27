# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#36712

parser = all_parsers

data = """a,b
1,2.5
,
"""
result = parser.read_csv(StringIO(data), use_nullable_dtypes=True, dtype="float64")
expected = DataFrame({"a": [1.0, np.nan], "b": [2.5, np.nan]})
tm.assert_frame_equal(result, expected)

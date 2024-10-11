# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#491496
data = """a,b
1,2
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), dtype="Int64", use_nullable_dtypes=True)
expected = DataFrame({"a": [1], "b": 2}, dtype="Int64")
tm.assert_frame_equal(result, expected)

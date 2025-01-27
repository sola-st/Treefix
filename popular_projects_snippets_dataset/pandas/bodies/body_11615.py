# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
# see gh-10153
parser = all_parsers
data = """a,b,c
1,a,3.4
1,a,3.4
2,b,4.5"""
expected = DataFrame(
    {"a": [1, 1, 2], "b": Categorical(["a", "a", "b"]), "c": [3.4, 3.4, 4.5]}
)
actual = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(actual, expected)

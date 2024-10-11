# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
# see gh-10153
parser = all_parsers
data = """a,b,c
1,b,3.4
1,nan,3.4
2,a,4.5"""
expected = DataFrame(
    {
        "a": Categorical(["1", "1", "2"]),
        "b": Categorical(["b", np.nan, "a"]),
        "c": Categorical(["3.4", "3.4", "4.5"]),
    }
)
actual = parser.read_csv(StringIO(data), dtype="category")
tm.assert_frame_equal(actual, expected)

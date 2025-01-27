# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
parser = all_parsers
data = """a,b
1,a
1,b
1,b
2,c"""
dtype = CategoricalDtype(["c", "b", "a"])
expected = DataFrame(
    {
        "a": [1, 1, 1, 2],
        "b": Categorical(["a", "b", "b", "c"], categories=["c", "b", "a"]),
    }
)

result = parser.read_csv(StringIO(data), dtype={"b": dtype})
tm.assert_frame_equal(result, expected)

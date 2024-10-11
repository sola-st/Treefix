# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
parser = all_parsers
data = """a,b
1,a
1,b
1,b
2,c"""
expected = DataFrame(
    {
        "a": [1, 1, 1, 2],
        "b": Categorical(
            ["a", "b", "b", "c"], categories=categories, ordered=ordered
        ),
    }
)

dtype = {"b": CategoricalDtype(categories=categories, ordered=ordered)}
result = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(result, expected)

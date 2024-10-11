# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_get_numeric_data.py
# numeric and object columns

df = DataFrame(
    {
        "a": [1, 2, 3],
        "b": [True, False, True],
        "c": ["foo", "bar", "baz"],
        "d": [None, None, None],
        "e": [3.14, 0.577, 2.773],
    }
)
result = df._get_numeric_data()
tm.assert_index_equal(result.columns, Index(["a", "b", "e"]))

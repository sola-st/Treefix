# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH21892 GH33205
expected = DataFrame.from_dict(
    {
        "Integer": Series([1, 2, 3], dtype="int64"),
        "Float": Series([None, 2.0, 3.0], dtype="float64"),
        "Object": Series([None, "", "c"], dtype="object"),
        "Bool": Series([True, False, True], dtype="bool"),
        "Category": Series(["a", "b", None], dtype="category"),
        "Datetime": Series(
            ["2020-01-01", None, "2020-01-03"], dtype="datetime64[ns]"
        ),
    }
)
dfjson = expected.to_json(orient=orient)
result = read_json(
    dfjson,
    orient=orient,
    dtype={
        "Integer": "int64",
        "Float": "float64",
        "Object": "object",
        "Bool": "bool",
        "Category": "category",
        "Datetime": "datetime64[ns]",
    },
)
tm.assert_frame_equal(result, expected)

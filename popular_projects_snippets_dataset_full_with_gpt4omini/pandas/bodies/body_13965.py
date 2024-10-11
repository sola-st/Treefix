# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# GH#50099
df = DataFrame({"x": ["foo", "bar", "baz"], "y": ["a", "b", "c"], "z": [1, 2, 3]})
df = df.astype(
    {"x": "string[pyarrow]", "y": "string[python]", "z": "int64[pyarrow]"}
)
result = df.dtypes.to_string()
expected = dedent(
    """\
        x    string[pyarrow]
        y     string[python]
        z     int64[pyarrow]"""
)
assert result == expected

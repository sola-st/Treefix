# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# https://github.com/pandas-dev/pandas/issues/36775
dtype = float_ea_dtype
s = Series([0.0, 1.0, None], dtype=dtype)
result = s.to_string()
expected = dedent(
    """\
        0     0.0
        1     1.0
        2    <NA>"""
)
assert result == expected

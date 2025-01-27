# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
df = DataFrame({"c/\u03c3": [1, 2, 3]})
result = df.to_string(formatters={"c/\u03c3": str})
expected = dedent(
    """\
          c/\u03c3
        0   1
        1   2
        2   3"""
)
assert result == expected

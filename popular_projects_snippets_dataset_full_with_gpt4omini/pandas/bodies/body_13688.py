# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_string.py
result = styler.concat(styler.data.agg(["sum"]).style).to_string()
expected = dedent(
    """\
     A B C
    0 0 -0.61 ab
    1 1 -1.22 cd
    sum 1 -1.830000 abcd
    """
)
assert result == expected

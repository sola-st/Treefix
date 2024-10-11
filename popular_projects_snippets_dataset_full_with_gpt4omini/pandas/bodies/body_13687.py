# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_string.py
result = styler.to_string(delimiter=";")
expected = dedent(
    """\
    ;A;B;C
    0;0;-0.61;ab
    1;1;-1.22;cd
    """
)
assert result == expected

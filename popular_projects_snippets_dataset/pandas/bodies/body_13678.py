# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
expected = {
    (0, 0): [("background-color", "yellow")],
    (0, 1): [("background-color", "yellow")],
}
result = styler.highlight_between(**kwargs)._compute().ctx
assert result == expected

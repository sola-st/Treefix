# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
result = styler.highlight_null()._compute().ctx
expected = {
    (1, 0): [("background-color", "red")],
    (1, 1): [("background-color", "red")],
}
assert result == expected

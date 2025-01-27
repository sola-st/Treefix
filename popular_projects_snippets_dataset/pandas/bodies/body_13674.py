# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
# GH 31345
result = (
    styler.highlight_null(color="red", subset=["A"])
    .highlight_null(color="green", subset=["B"])
    ._compute()
    .ctx
)
expected = {
    (1, 0): [("background-color", "red")],
    (1, 1): [("background-color", "green")],
}
assert result == expected

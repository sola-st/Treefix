# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
# GH 42750
expected = {
    (1, 0): [("background-color", "yellow")],
    (1, 1): [("background-color", "yellow")],
}
if axis == 1:
    expected.update({(2, 1): [("background-color", "yellow")]})

if f == "highlight_max":
    df = DataFrame({"a": [NA, 1, None], "b": [np.nan, 1, -1]})
else:
    df = DataFrame({"a": [NA, -1, None], "b": [np.nan, -1, 1]})

result = getattr(df.style, f)(axis=axis)._compute().ctx
assert result == expected

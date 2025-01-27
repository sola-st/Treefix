# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
expected = {(2, 0): [("background-color", "red")]}
if f == "highlight_min":
    df = -df
result = getattr(df.style, f)(**kwargs)._compute().ctx
assert result == expected

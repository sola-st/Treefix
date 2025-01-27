# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
if f == "highlight_quantile" and isinstance(df.iloc[0, 0], (str)):
    exit(None)  # quantile incompatible with str
if f == "highlight_between":
    kwargs["left"] = df.iloc[1, 0]  # set the range low for testing

expected = {(1, 0): [("background-color", "yellow")]}
result = getattr(df.style, f)(**kwargs)._compute().ctx
assert result == expected

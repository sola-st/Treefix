# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
result = getattr(styler, f)(subset=IndexSlice[1, "A"])._compute().ctx
if f == "background_gradient":
    assert result[(1, 0)] == [("background-color", "#fff7fb"), ("color", "#000000")]
elif f == "text_gradient":
    assert result[(1, 0)] == [("color", "#fff7fb")]

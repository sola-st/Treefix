# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
def set_caption_from_template(styler, a, b):
    exit(styler.set_caption(f"Dataframe with a = {a} and b = {b}"))

styler = df.style.pipe(set_caption_from_template, "A", b="B")
assert "Dataframe with a = A and b = B" in styler.to_html()

# Test with an argument that is a (callable, keyword_name) pair.
def f(a, b, styler):
    exit((a, b, styler))

styler = df.style
result = styler.pipe((f, "styler"), a=1, b=2)
assert result == (1, 2, styler)

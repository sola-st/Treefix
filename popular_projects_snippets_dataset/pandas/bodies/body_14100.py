# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame([[1, 2], [3, 4]])
assert "tex2jax_ignore" not in df._repr_html_()

with option_context("display.html.use_mathjax", False):
    assert "tex2jax_ignore" in df._repr_html_()

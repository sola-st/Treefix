# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# gh-19824 / 41395
assert "tex2jax_ignore" not in styler._repr_html_()

with option_context("styler.html.mathjax", False):
    assert "tex2jax_ignore" in styler._repr_html_()

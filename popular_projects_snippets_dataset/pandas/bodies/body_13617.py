# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
assert "<style" in styler._repr_html_()[:6]
assert styler._repr_latex_() is None
with option_context("styler.render.repr", "latex"):
    assert "\\begin{tabular}" in styler._repr_latex_()[:15]
    assert styler._repr_html_() is None

# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
pytest.importorskip("jinja2")  # uses Styler implementation
result = r"""\begin{tabular}{ll}
\toprule
 & 0 \\
\midrule
0 & $\alpha$ \\
1 & b \\
2 & c \\
\bottomrule
\end{tabular}
"""
with option_context(
    "display.latex.escape", False, "styler.render.repr", "latex"
):
    s = Series([r"$\alpha$", "b", "c"])
    assert result == s._repr_latex_()

assert s._repr_latex_() is None

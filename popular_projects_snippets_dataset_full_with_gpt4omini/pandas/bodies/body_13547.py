# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 21625
df = DataFrame({"x": [0.19999]})
result = df.to_latex(float_format="%.3f")
expected = _dedent(
    r"""
            \begin{tabular}{lr}
            \toprule
             & x \\
            \midrule
            0 & 0.200 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

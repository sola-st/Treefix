# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 22270
df = DataFrame({"x": [100.0]})
result = df.to_latex(float_format="%.0f")
expected = _dedent(
    r"""
            \begin{tabular}{lr}
            \toprule
             & x \\
            \midrule
            0 & 100 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

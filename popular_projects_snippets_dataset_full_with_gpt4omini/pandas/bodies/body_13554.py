# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame({("x", "y"): ["a"]})
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{ll}
            \toprule
             & x \\
             & y \\
            \midrule
            0 & a \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

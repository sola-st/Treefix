# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame({("x", "y"): ["a"]}).T
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{lll}
            \toprule
             &  & 0 \\
            \midrule
            x & y & a \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 7124
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
result = df.to_latex(header=["AA", "BB"], index=False)
expected = _dedent(
    r"""
            \begin{tabular}{rl}
            \toprule
            AA & BB \\
            \midrule
            1 & b1 \\
            2 & b2 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

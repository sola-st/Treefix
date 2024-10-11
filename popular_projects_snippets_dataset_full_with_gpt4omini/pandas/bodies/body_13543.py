# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 7124
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
result = df.to_latex(header=["$A$", "$B$"], escape=False)
expected = _dedent(
    r"""
            \begin{tabular}{lrl}
            \toprule
             & $A$ & $B$ \\
            \midrule
            0 & 1 & b1 \\
            1 & 2 & b2 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

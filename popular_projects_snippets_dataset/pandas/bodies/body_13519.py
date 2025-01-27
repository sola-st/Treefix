# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 16707
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
result = df.to_latex(bold_rows=True)
expected = _dedent(
    r"""
            \begin{tabular}{lrl}
            \toprule
             & a & b \\
            \midrule
            \textbf{0} & 1 & b1 \\
            \textbf{1} & 2 & b2 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

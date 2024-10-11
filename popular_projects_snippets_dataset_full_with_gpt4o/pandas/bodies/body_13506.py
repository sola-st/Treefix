# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame()
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{l}
            \toprule
            \midrule
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

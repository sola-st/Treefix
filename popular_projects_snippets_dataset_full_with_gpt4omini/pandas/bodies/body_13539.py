# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
result = df_with_symbols.to_latex(escape=False)
expected = _dedent(
    r"""
            \begin{tabular}{lll}
            \toprule
             & co$e^x$ & co^l1 \\
            \midrule
            a & a & a \\
            b & b & b \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

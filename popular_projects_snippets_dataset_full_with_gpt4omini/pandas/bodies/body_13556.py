# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
result = multiindex_frame.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{llrrrr}
            \toprule
             &  & 0 & 1 & 2 & 3 \\
            \midrule
            c1 & 0 & 0 & 1 & 2 & 3 \\
             & 1 & 4 & 5 & 6 & 7 \\
            c2 & 0 & 0 & 1 & 2 & 3 \\
             & 1 & 4 & 5 & 6 & 7 \\
            c3 & 0 & 0 & 1 & 2 & 3 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

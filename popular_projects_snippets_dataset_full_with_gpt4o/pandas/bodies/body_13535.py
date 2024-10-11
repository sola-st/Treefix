# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 25436
result = df_short.to_latex(longtable=True, label=label_longtable)
expected = _dedent(
    r"""
            \begin{longtable}{lrl}
            \label{tab:longtable} \\
            \toprule
             & a & b \\
            \midrule
            \endfirsthead
            \toprule
             & a & b \\
            \midrule
            \endhead
            \midrule
            \multicolumn{3}{r}{Continued on next page} \\
            \midrule
            \endfoot
            \bottomrule
            \endlastfoot
            0 & 1 & b1 \\
            1 & 2 & b2 \\
            \end{longtable}
            """
)
assert result == expected

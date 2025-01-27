# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 25436
# test when no caption and no label is provided
# is performed by test_to_latex_longtable()
result = df_short.to_latex(longtable=True, caption=caption_longtable)
expected = _dedent(
    r"""
            \begin{longtable}{lrl}
            \caption{a table in a \texttt{longtable} environment} \\
            \toprule
             & a & b \\
            \midrule
            \endfirsthead
            \caption[]{a table in a \texttt{longtable} environment} \\
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

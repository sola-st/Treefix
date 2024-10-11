# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# test when the caption, the short_caption and the label are provided
result = df_short.to_latex(
    longtable=True,
    caption=(caption_longtable, short_caption),
    label=label_longtable,
)
expected = _dedent(
    r"""
\begin{longtable}{lrl}
\caption[a table]{a table in a \texttt{longtable} environment} \label{tab:longtable} \\
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

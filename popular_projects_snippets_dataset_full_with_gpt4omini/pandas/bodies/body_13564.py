# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
multicolumn_frame.index = multicolumn_frame.T.index
result = multicolumn_frame.T.to_latex(
    multirow=True,
    multicolumn=True,
    multicolumn_format="c",
)
expected = _dedent(
    r"""
            \begin{tabular}{llrrrrr}
            \toprule
             &  & \multicolumn{2}{c}{c1} & \multicolumn{2}{c}{c2} & c3 \\
             &  & 0 & 1 & 0 & 1 & 0 \\
            \midrule
            \multirow[t]{2}{*}{c1} & 0 & 0 & 1 & 2 & 3 & 4 \\
             & 1 & 5 & 6 & 7 & 8 & 9 \\
            \cline{1-7}
            \multirow[t]{2}{*}{c2} & 0 & 0 & 1 & 2 & 3 & 4 \\
             & 1 & 5 & 6 & 7 & 8 & 9 \\
            \cline{1-7}
            c3 & 0 & 0 & 1 & 2 & 3 & 4 \\
            \cline{1-7}
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
result = multicolumn_frame.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{lrrrrr}
            \toprule
             & \multicolumn{2}{l}{c1} & \multicolumn{2}{l}{c2} & c3 \\
             & 0 & 1 & 0 & 1 & 0 \\
            \midrule
            0 & 0 & 5 & 0 & 5 & 0 \\
            1 & 1 & 6 & 1 & 6 & 1 \\
            2 & 2 & 7 & 2 & 7 & 2 \\
            3 & 3 & 8 & 3 & 8 & 3 \\
            4 & 4 & 9 & 4 & 9 & 4 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

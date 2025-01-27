# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 14184
df = multiindex_frame.T
df.columns.names = ["a", "b"]
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{lrrrrr}
            \toprule
            a & \multicolumn{2}{l}{c1} & \multicolumn{2}{l}{c2} & c3 \\
            b & 0 & 1 & 0 & 1 & 0 \\
            \midrule
            0 & 0 & 4 & 0 & 4 & 0 \\
            1 & 1 & 5 & 1 & 5 & 1 \\
            2 & 2 & 6 & 2 & 6 & 2 \\
            3 & 3 & 7 & 3 & 7 & 3 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

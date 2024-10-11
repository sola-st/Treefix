# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 10660
df = DataFrame({"a": [0, 0, 1, 1], "b": list("abab"), "c": [1, 2, 3, 4]})
result = df.groupby("a").describe().to_latex(float_format="{:.1f}".format)
expected = _dedent(
    r"""
            \begin{tabular}{lrrrrrrrr}
            \toprule
             & \multicolumn{8}{l}{c} \\
             & count & mean & std & min & 25\% & 50\% & 75\% & max \\
            a &  &  &  &  &  &  &  &  \\
            \midrule
            0 & 2.0 & 1.5 & 0.7 & 1.0 & 1.2 & 1.5 & 1.8 & 2.0 \\
            1 & 2.0 & 3.5 & 0.7 & 3.0 & 3.2 & 3.5 & 3.8 & 4.0 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected

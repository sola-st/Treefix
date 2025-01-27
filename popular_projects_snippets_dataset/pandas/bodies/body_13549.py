# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame(
    [
        ["A", 1.2225],
        ["A", None],
    ],
    columns=["Group", "Data"],
)
result = df.to_latex(na_rep=na_rep, float_format="{:.2f}".format)
expected = _dedent(
    rf"""
            \begin{{tabular}}{{llr}}
            \toprule
             & Group & Data \\
            \midrule
            0 & A & 1.22 \\
            1 & A & {na_rep} \\
            \bottomrule
            \end{{tabular}}
            """
)
assert result == expected

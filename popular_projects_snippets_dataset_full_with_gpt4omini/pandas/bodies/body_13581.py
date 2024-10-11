# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
expected = dedent(
    """\
        \\begin{tabular}{lrrl}
        \\toprule
         & A & B & C \\\\
        \\midrule
        0 & 0 & -0.61 & ab \\\\
        1 & 1 & -1.22 & cd \\\\
        \\bottomrule
        \\end{tabular}
        """
)
assert styler.to_latex(hrules=True) == expected

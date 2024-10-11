# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
styler.set_table_styles(
    [
        {"selector": "toprule", "props": ":hline"},
        {"selector": "bottomrule", "props": ":otherline"},
    ]
)  # no midrule
expected = dedent(
    """\
        \\begin{tabular}{lrrl}
        \\hline
         & A & B & C \\\\
        0 & 0 & -0.61 & ab \\\\
        1 & 1 & -1.22 & cd \\\\
        \\otherline
        \\end{tabular}
        """
)
assert styler.to_latex() == expected

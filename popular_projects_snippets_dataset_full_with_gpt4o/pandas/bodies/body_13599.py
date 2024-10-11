# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
styler.hide(axis="index")
expected = dedent(
    """\
        \\begin{tabular}{rrl}
        A & B & C \\\\
        0 & -0.61 & ab \\\\
        1 & -1.22 & cd \\\\
        \\end{tabular}
        """
)
assert styler.to_latex() == expected

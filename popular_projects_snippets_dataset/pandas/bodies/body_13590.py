# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
styler.highlight_max(props="itshape:;Huge:--wrap;")
expected = dedent(
    """\
        \\begin{tabular}{lrrl}
         & A & B & C \\\\
        0 & 0 & \\itshape {\\Huge -0.61} & ab \\\\
        1 & \\itshape {\\Huge 1} & -1.22 & \\itshape {\\Huge cd} \\\\
        \\end{tabular}
        """
)
assert expected == styler.to_latex()

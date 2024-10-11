# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# GH 43637
styler.hide([0], axis=0)
result = styler.to_latex()
expected = dedent(
    """\
    \\begin{tabular}{lrrl}
     & A & B & C \\\\
    1 & 1 & -1.22 & cd \\\\
    \\end{tabular}
    """
)
assert expected == result

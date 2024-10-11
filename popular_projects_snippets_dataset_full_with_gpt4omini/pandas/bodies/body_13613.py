# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
result = styler.to_latex(environment="longtable")
expected = dedent(
    """\
        \\begin{longtable}{lrrl}
         & A & B & C \\\\
        \\endfirsthead
         & A & B & C \\\\
        \\endhead
        \\multicolumn{4}{r}{Continued on next page} \\\\
        \\endfoot
        \\endlastfoot
        0 & 0 & -0.61 & ab \\\\
        1 & 1 & -1.22 & cd \\\\
        \\end{longtable}
    """
)
assert result == expected

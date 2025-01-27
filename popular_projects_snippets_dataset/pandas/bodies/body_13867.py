# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_non_unique.py
result = styler.to_latex()
assert result == dedent(
    """\
        \\begin{tabular}{lrrr}
         & c & d & d \\\\
        i & 1.000000 & 2.000000 & 3.000000 \\\\
        j & 4.000000 & 5.000000 & 6.000000 \\\\
        j & 7.000000 & 8.000000 & 9.000000 \\\\
        \\end{tabular}
    """
)

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# tests hidden row recursion and applied styles
styler1 = DataFrame([[1], [9]]).style.hide([1]).highlight_min(color="red")
styler2 = DataFrame([[9], [2]]).style.hide([0]).highlight_min(color="green")
styler3 = DataFrame([[3], [9]]).style.hide([1]).highlight_min(color="blue")

result = styler1.concat(styler2).concat(styler3).to_latex(convert_css=True)
expected = dedent(
    """\
    \\begin{tabular}{lr}
     & 0 \\\\
    0 & {\\cellcolor{red}} 1 \\\\
    1 & {\\cellcolor{green}} 2 \\\\
    0 & {\\cellcolor{blue}} 3 \\\\
    \\end{tabular}
    """
)
assert result == expected

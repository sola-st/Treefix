# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
assert "\\begin{table}[h!]" in styler.to_latex(position="h!")
assert "\\end{table}" in styler.to_latex(position="h!")
styler.set_table_styles([{"selector": "position", "props": ":b!"}])
assert "\\begin{table}[b!]" in styler.to_latex()
assert "\\end{table}" in styler.to_latex()

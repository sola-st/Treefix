# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# default setting is already tested in `test_latex_minimal_tabular`
styler.set_table_styles([{"selector": "column_format", "props": ":cccc"}])

assert "\\begin{tabular}{rrrr}" in styler.to_latex(column_format="rrrr")
styler.set_table_styles([{"selector": "column_format", "props": ":r|r|cc"}])
assert "\\begin{tabular}{r|r|cc}" in styler.to_latex()

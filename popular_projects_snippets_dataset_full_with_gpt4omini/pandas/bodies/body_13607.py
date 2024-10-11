# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
result = styler.to_latex(caption=("full cap", "short cap"))
assert "\\caption[short cap]{full cap}" in result

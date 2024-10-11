# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
cell_style = [("<command>", f"<options>{wrap_arg}")]
assert _parse_latex_cell_styles(cell_style, "<display_value>") == expected

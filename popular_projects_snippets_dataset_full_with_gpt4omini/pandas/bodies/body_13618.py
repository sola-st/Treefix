# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
with option_context(f"styler.latex.{option}", False):
    latex_false = styler.to_latex()
with option_context(f"styler.latex.{option}", True):
    latex_true = styler.to_latex()
assert latex_false != latex_true  # options are reactive under to_latex(*no_args)

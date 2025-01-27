# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
assert "{} & {A} & {B} & {C} \\\\" in styler.to_latex(siunitx=True)
assert " & A & B & C \\\\" in styler.to_latex()  # default siunitx=False

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
styler.applymap_index(lambda x: "font-weight: bold;", axis=axis)
for label in getattr(styler, axis):
    assert f"\\bfseries {label}" in styler.to_latex(convert_css=True)

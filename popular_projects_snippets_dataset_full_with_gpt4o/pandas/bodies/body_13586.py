# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
assert "\n\\label{text}" in styler.to_latex(label="text", environment=env)
styler.set_table_styles([{"selector": "label", "props": ":{more §text}"}])
assert "\n\\label{more :text}" in styler.to_latex(environment=env)

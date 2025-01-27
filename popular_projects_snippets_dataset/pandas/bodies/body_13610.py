# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
css = [("command", "option--latex--wrap")]
expected = [("command", "option--wrap")]
result = _parse_latex_css_conversion(css)
assert result == expected

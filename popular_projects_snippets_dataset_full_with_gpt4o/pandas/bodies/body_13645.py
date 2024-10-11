# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
result = styler.to_html(bold_headers=True)
assert "th {\n  font-weight: bold;\n}" in result
result = styler.to_html()
assert "th {\n  font-weight: bold;\n}" not in result

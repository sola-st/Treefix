# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
result = styler.to_html(doctype_html=False)
assert "<html>" not in result
assert "<body>" not in result
assert "<!DOCTYPE html>" not in result
assert "<head>" not in result

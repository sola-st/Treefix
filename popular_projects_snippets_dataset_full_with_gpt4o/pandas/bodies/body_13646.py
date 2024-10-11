# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
result = styler.to_html(caption="foo bar")
assert "<caption>foo bar</caption>" in result
result = styler.to_html()
assert "<caption>foo bar</caption>" not in result

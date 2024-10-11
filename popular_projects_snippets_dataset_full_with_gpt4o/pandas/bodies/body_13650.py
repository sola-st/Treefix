# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
styler.set_caption(("full cap", "short cap"))
assert "<caption>full cap</caption>" in styler.to_html()

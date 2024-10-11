# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
styler = Styler(df, caption="foo")
result = styler.to_html()
assert all(["caption" in result, "foo" in result])

styler = df.style
result = styler.set_caption("baz")
assert styler is result
assert styler.caption == "baz"

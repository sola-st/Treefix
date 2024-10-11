# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
style = [{"selector": "th", "props": [("foo", "bar")]}]  # default format
styler = Styler(df, table_styles=style)
result = " ".join(styler.to_html().split())
assert "th { foo: bar; }" in result

styler = df.style
result = styler.set_table_styles(style)
assert styler is result
assert styler.table_styles == style

# GH 39563
style = [{"selector": "th", "props": "foo:bar;"}]  # css string format
styler = df.style.set_table_styles(style)
result = " ".join(styler.to_html().split())
assert "th { foo: bar; }" in result

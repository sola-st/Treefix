# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
attributes = 'class="foo" data-bar'
styler = Styler(df, table_attributes=attributes)
result = styler.to_html()
assert 'class="foo" data-bar' in result

result = df.style.set_table_attributes(attributes).to_html()
assert 'class="foo" data-bar' in result

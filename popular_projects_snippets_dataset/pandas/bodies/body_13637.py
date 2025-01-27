# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
# make sure if templates are edited tests are updated as are setup fixtures
# to understand the dependency
with open("pandas/io/formats/templates/html.tpl") as file:
    result = file.read()
assert "{% include html_style_tpl %}" in result
assert "{% include html_table_tpl %}" in result

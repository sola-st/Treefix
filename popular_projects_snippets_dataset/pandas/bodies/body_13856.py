# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_tooltip.py
# GH 21266
result = styler.to_html()  # no set_tooltips() creates no <span>
assert '<style type="text/css">\n</style>' in result
assert '<span class="pd-t"></span>' not in result

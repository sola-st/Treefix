# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# see gh-17004
df = DataFrame([lorem_ipsum])
with option_context("display.max_colwidth", max_colwidth):
    result = getattr(df, method)()
expected = expected(max_colwidth)
assert expected in result

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_markdown.py
buf = StringIO()
s = pd.Series([1, 2, 3], name="foo")
s.to_markdown(buf=buf)
result = buf.getvalue()
assert result == (
    "|    |   foo |\n|---:|------:|\n|  0 |     1 "
    "|\n|  1 |     2 |\n|  2 |     3 |"
)

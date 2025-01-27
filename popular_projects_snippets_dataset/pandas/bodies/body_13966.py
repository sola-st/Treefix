# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_markdown.py
buf = StringIO()
df = pd.DataFrame([1, 2, 3])
df.to_markdown(buf=buf)
result = buf.getvalue()
assert (
    result == "|    |   0 |\n|---:|----:|\n|  0 |   1 |\n|  1 |   2 |\n|  2 |   3 |"
)

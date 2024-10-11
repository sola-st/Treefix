# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_markdown.py
buf = StringIO()
df = pd.DataFrame({"id": [], "first_name": [], "last_name": []}).set_index("id")
df.to_markdown(buf=buf)
result = buf.getvalue()
assert result == (
    "| id   | first_name   | last_name   |\n"
    "|------|--------------|-------------|"
)

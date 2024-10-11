# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame({"x": np.random.randn(5)})
html = df.to_html(bold_rows=False)
result = html[html.find("</thead>")]
assert "<strong" not in result

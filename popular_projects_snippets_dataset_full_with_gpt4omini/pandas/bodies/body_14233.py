# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = biggie_df_fixture
expected = df.to_html()
path = tmpdir.join("test.html")
df.to_html(path)
result = path.read()
assert result == expected

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
url = banklist_data
dfs = self.read_html(
    file_path_to_url(os.path.abspath(url)),
    match=re.compile(re.compile("Florida")),
    attrs={"id": "table"},
)
assert isinstance(dfs, list)
for df in dfs:
    assert isinstance(df, DataFrame)

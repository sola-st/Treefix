# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
dfs = self.read_html(banklist_data, attrs={"id": "table"})
for df in dfs:
    assert isinstance(df, DataFrame)

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df1 = self.read_html(banklist_data, match=".*Florida.*", attrs={"id": "table"})
df2 = self.read_html(banklist_data, match="Metcalf Bank", attrs={"id": "table"})

assert_framelist_equal(df1, df2)

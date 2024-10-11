# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
with open(spam_data, encoding="UTF-8") as f:
    data1 = StringIO(f.read())

with open(spam_data, encoding="UTF-8") as f:
    data2 = StringIO(f.read())

df1 = self.read_html(data1, match=".*Water.*")
df2 = self.read_html(data2, match="Unit")
assert_framelist_equal(df1, df2)

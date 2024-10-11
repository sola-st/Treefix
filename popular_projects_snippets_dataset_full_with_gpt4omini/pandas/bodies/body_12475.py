# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df1 = self.read_html(spam_data, match=".*Water.*", header=1, index_col=0)
df2 = self.read_html(spam_data, match="Unit", header=1, index_col=0)
assert_framelist_equal(df1, df2)

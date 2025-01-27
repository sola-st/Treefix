# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py

# 10892 infer_types removed
df1 = self.read_html(spam_data, match=".*Water.*", index_col=0)
df2 = self.read_html(spam_data, match="Unit", index_col=0)
assert_framelist_equal(df1, df2)

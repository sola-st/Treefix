# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df1 = self.read_html(spam_data, match=".*Water.*", skiprows={1, 2})
df2 = self.read_html(spam_data, match="Unit", skiprows={2, 1})

assert_framelist_equal(df1, df2)

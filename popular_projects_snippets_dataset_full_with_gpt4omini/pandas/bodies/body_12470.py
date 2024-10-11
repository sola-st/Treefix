# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df1 = self.read_html(spam_data, match=".*Water.*", skiprows=slice(2, 5))
df2 = self.read_html(spam_data, match="Unit", skiprows=slice(4, 1, -1))

assert_framelist_equal(df1, df2)

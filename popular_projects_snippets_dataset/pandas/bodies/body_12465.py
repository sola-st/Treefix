# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df1 = self.read_html(spam_data, match=".*Water.*", skiprows=range(2))
df2 = self.read_html(spam_data, match="Unit", skiprows=range(2))

assert_framelist_equal(df1, df2)

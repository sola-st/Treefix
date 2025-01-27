# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df1 = self.read_html(spam_data, match=".*Water.*")
df2 = self.read_html(spam_data, match="Unit")
assert_framelist_equal(df1, df2)

assert df1[0].iloc[0, 0] == "Proximates"
assert df1[0].columns[0] == "Nutrient"

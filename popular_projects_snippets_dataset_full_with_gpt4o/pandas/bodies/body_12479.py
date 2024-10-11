# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
with open(spam_data, encoding="UTF-8") as f:
    df1 = self.read_html(f, match=".*Water.*")

with open(spam_data, encoding="UTF-8") as f:
    df2 = self.read_html(f, match="Unit")

assert_framelist_equal(df1, df2)

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
url = (
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/"
    "pandas/tests/io/data/html/spam.html"
)
df1 = self.read_html(url, match=".*Water.*")
df2 = self.read_html(url, match="Unit")

assert_framelist_equal(df1, df2)

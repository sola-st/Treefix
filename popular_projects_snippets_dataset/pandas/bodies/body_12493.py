# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
url = "https://docs.python.org/2/"
dfs = self.read_html(url, match="Python")
assert len(dfs) > 1

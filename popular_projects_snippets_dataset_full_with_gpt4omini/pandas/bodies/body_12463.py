# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df = self.read_html(spam_data, match=".*Water.*", header=2)[0]
assert df.columns[0] == "Proximates"
assert not df.empty

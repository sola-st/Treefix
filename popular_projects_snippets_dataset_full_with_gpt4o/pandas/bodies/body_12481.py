# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
msg = (
    "Name or service not known|Temporary failure in name resolution|"
    "No tables found"
)
with pytest.raises((URLError, ValueError), match=msg):
    self.read_html("http://www.a23950sdfa908sd.com", match=".*Water.*")

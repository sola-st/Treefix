# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
with pytest.raises(URLError, match="urlopen error unknown url type: git"):
    self.read_html("git://github.com", match=".*Water.*")

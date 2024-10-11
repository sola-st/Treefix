# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
msg = r"\(you passed a negative value\)"
with pytest.raises(ValueError, match=msg):
    self.read_html(spam_data, match="Water", skiprows=-1)

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
with pytest.raises(TypeError, match=("is not a valid type for skipping rows")):
    self.read_html(spam_data, match=".*Water.*", skiprows="asdf")

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
msg = "values can be 'both', 'left', 'right', or 'neither'"
with pytest.raises(ValueError, match=msg):
    styler.highlight_between(inclusive="badstring")._compute()

with pytest.raises(ValueError, match=msg):
    styler.highlight_between(inclusive=1)._compute()

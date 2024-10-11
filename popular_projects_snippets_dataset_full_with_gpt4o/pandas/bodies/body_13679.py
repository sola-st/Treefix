# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
msg = f"supplied '{arg}' is not correct shape"
with pytest.raises(ValueError, match=msg):
    styler.highlight_between(**{arg: map, "axis": axis})._compute()

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
msg = "`caption` must be either a string or 2-tuple of strings."
with pytest.raises(ValueError, match=msg):
    mi_styler.set_caption(caption)

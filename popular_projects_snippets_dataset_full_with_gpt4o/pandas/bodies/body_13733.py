# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
with pytest.raises(TypeError, match="expected str or callable"):
    getattr(styler, func)(formatter)

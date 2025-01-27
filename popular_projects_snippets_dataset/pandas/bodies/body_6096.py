# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
with pytest.raises(ValueError, match=""):
    data.take([0, -2], fill_value=na_value, allow_fill=True)

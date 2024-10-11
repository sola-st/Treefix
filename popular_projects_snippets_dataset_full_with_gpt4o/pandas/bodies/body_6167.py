# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
msg = "Length of 'value' does not match."
with pytest.raises(ValueError, match=msg):
    data_missing.fillna(data_missing.take([1]))

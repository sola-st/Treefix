# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
msg = ""  # messages vary by subclass, so we do not test it
with pytest.raises((ValueError, TypeError), match=msg):
    data[0] = invalid_scalar

with pytest.raises((ValueError, TypeError), match=msg):
    data[:] = invalid_scalar

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# GH 28406
s = cls(values)

msg = "Cannot (cast|convert)"
with pytest.raises((ValueError, TypeError), match=msg):
    s.astype(int)

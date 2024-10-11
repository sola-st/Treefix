# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
# GH 26447
msg = "^'str' object cannot be interpreted as an integer$"
with pytest.raises(TypeError, match=msg):
    bytes(unicode_container)

# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
msg = "unhashable type: 'Series'"
with pytest.raises(TypeError, match=msg):
    hash(ser)

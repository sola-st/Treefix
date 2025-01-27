# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
g = test_frame.resample("H")
# 'A' should not be referenced as a bad column...
# will have to rethink regex if you change message!
msg = r"^\"Columns not found: 'D'\"$"
with pytest.raises(KeyError, match=msg):
    g[key]

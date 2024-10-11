# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
msg = "Could not convert foo to numeric"
with pytest.raises(TypeError, match=msg):
    nanops._ensure_numeric("foo")

# with the wrong type, python raises TypeError for us
msg = "argument must be a string or a number"
with pytest.raises(TypeError, match=msg):
    nanops._ensure_numeric({})
with pytest.raises(TypeError, match=msg):
    nanops._ensure_numeric([])

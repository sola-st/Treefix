# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 40543
df = DataFrame({"a": [None]})
msg = re.escape("int() argument must be a string")
with pytest.raises(TypeError, match=msg):
    df.agg({"a": int})

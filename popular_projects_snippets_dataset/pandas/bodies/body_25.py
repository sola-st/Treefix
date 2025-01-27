# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH#34377
df = DataFrame({"a": [None]})
msg = "argument must be a"
with pytest.raises(TypeError, match=msg):
    df.transform({"a": int})

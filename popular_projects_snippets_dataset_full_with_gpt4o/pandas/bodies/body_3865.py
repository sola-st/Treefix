# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH 26447
df = DataFrame({"A": ["abc"]})
msg = "^'str' object cannot be interpreted as an integer$"
with pytest.raises(TypeError, match=msg):
    bytes(df)

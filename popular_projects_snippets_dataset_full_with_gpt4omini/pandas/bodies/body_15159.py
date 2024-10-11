# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# GH 26447
df = Series(["abc"], name="abc")
msg = "^'str' object cannot be interpreted as an integer$"
with pytest.raises(TypeError, match=msg):
    bytes(df)

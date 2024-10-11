# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 18634
# API: replace() should raise an exception if invalid argument is given
df = DataFrame({"one": ["a", "b ", "c"], "two": ["d ", "e ", "f "]})
msg = (
    r"Expecting 'to_replace' to be either a scalar, array-like, "
    r"dict or None, got invalid type.*"
)
with pytest.raises(TypeError, match=msg):
    df.replace(lambda x: x.strip())

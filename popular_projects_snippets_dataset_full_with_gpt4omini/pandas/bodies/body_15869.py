# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 18634
# API: replace() should raise an exception if invalid argument is given
series = pd.Series(["a", "b", "c "])
msg = (
    r"Expecting 'to_replace' to be either a scalar, array-like, "
    r"dict or None, got invalid type.*"
)
with pytest.raises(TypeError, match=msg):
    series.replace(lambda x: x.strip())

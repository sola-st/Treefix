# Extracted from ./data/repos/pandas/pandas/tests/strings/test_cat.py
# GH 28277
ps = Series(["AbC", "de", "FGHI", "j", "kLLLm"])

message = re.escape(
    "others must be Series, Index, DataFrame, np.ndarray "
    "or list-like (either containing only strings or "
    "containing only objects of type Series/Index/"
    "np.ndarray[1-dim])"
)
with pytest.raises(TypeError, match=message):
    ps.str.cat(others=ps.str)

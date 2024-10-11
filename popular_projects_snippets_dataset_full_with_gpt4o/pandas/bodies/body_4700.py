# Extracted from ./data/repos/pandas/pandas/tests/strings/test_cat.py
# GH 22722
s = Series(["a", "b", "c"])
t = box(data)

msg = "Concatenation requires list-likes containing only strings.*"
with pytest.raises(TypeError, match=msg):
    # need to use outer and na_rep, as otherwise Index would not raise
    s.str.cat(t, join="outer", na_rep="-")

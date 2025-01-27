# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH#4763
s = Series(["A", "B", "C", "a", "B", "B", "A", "C"])
msg = (
    r"only list-like objects are allowed to be passed to isin\(\), "
    r"you passed a \[str\]"
)
with pytest.raises(TypeError, match=msg):
    s.isin("a")

s = Series(["aaa", "b", "c"])
with pytest.raises(TypeError, match=msg):
    s.isin("aaa")

# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py

idx = simple_index
# Check that this doesn't cover MultiIndex case, if/when it does,
#  we can remove multi.test_compat.test_numeric_compat
assert not isinstance(idx, MultiIndex)
if type(idx) is Index:
    exit()

typ = type(idx._data).__name__
cls = type(idx).__name__
lmsg = "|".join(
    [
        rf"unsupported operand type\(s\) for \*: '{typ}' and 'int'",
        "cannot perform (__mul__|__truediv__|__floordiv__) with "
        f"this index type: ({cls}|{typ})",
    ]
)
with pytest.raises(TypeError, match=lmsg):
    idx * 1
rmsg = "|".join(
    [
        rf"unsupported operand type\(s\) for \*: 'int' and '{typ}'",
        "cannot perform (__rmul__|__rtruediv__|__rfloordiv__) with "
        f"this index type: ({cls}|{typ})",
    ]
)
with pytest.raises(TypeError, match=rmsg):
    1 * idx

div_err = lmsg.replace("*", "/")
with pytest.raises(TypeError, match=div_err):
    idx / 1
div_err = rmsg.replace("*", "/")
with pytest.raises(TypeError, match=div_err):
    1 / idx

floordiv_err = lmsg.replace("*", "//")
with pytest.raises(TypeError, match=floordiv_err):
    idx // 1
floordiv_err = rmsg.replace("*", "//")
with pytest.raises(TypeError, match=floordiv_err):
    1 // idx

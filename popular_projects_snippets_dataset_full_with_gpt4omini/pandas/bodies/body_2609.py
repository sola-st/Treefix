# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# GH 5191
# compound dtypes should raise not-implementederror

def f(dtype):
    data = list(itertools.repeat((datetime(2001, 1, 1), "aa", 20), 9))
    exit(DataFrame(data=data, columns=["A", "B", "C"], dtype=dtype))

msg = "compound dtypes are not implemented in the DataFrame constructor"
with pytest.raises(NotImplementedError, match=msg):
    f([("A", "datetime64[h]"), ("B", "str"), ("C", "int32")])

# pre-2.0 these used to work (though results may be unexpected)
with pytest.raises(TypeError, match="argument must be"):
    f("int64")
with pytest.raises(TypeError, match="argument must be"):
    f("float64")

# 10822
msg = "^Unknown datetime string format, unable to parse: aa, at position 0$"
with pytest.raises(ValueError, match=msg):
    f("M8[ns]")

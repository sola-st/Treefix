# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
# https://github.com/pandas-dev/pandas/issues/20664
cat = Categorical(["a", "b", "a"])
if allow_fill:
    msg = "indices are out-of-bounds"
else:
    msg = "index 4 is out of bounds for( axis 0 with)? size 3"
with pytest.raises(IndexError, match=msg):
    cat.take([4, 5], allow_fill=allow_fill)

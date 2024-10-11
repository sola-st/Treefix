# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
# https://github.com/pandas-dev/pandas/issues/23296
cat = Categorical(["a", "b", "c"])
xpr = r"Cannot setitem on a Categorical with a new category \(d\)"
with pytest.raises(TypeError, match=xpr):
    cat.take([0, 1, -1], fill_value="d", allow_fill=True)

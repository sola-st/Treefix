# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 19016: categorical data
data = Categorical(list("01234abcde"), ordered=True)
msg = (
    "category, object, and string subtypes are not supported "
    "for IntervalIndex"
)
with pytest.raises(TypeError, match=msg):
    IntervalIndex.from_arrays(data[:-1], data[1:])

# unequal length
left = [0, 1, 2]
right = [2, 3]
msg = "left and right must have the same length"
with pytest.raises(ValueError, match=msg):
    IntervalIndex.from_arrays(left, right)

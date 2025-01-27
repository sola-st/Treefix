# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 19016: categorical data
data = Categorical(list("01234abcde"), ordered=True)
msg = (
    "category, object, and string subtypes are not supported "
    "for IntervalIndex"
)
with pytest.raises(TypeError, match=msg):
    IntervalIndex.from_breaks(data)

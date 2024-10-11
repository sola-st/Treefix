# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
left = Index([1, 2, 3])
right = Index([True, False], dtype=object)

msg = "Cannot compare dtypes int64 and bool"
with pytest.raises(TypeError, match=msg):
    left.asof(right[0])
# TODO: should right.asof(left[0]) also raise?

with pytest.raises(InvalidIndexError, match=re.escape(str(right))):
    left.asof(right)

with pytest.raises(InvalidIndexError, match=re.escape(str(left))):
    right.asof(left)

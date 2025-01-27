# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
msg = "RangeIndex\\(\\.\\.\\.\\) must be called with integers"
with pytest.raises(TypeError, match=msg):
    RangeIndex()

with pytest.raises(TypeError, match=msg):
    RangeIndex(name="Foo")

# we don't allow on a bare Index
msg = (
    r"Index\(\.\.\.\) must be called with a collection of some "
    r"kind, 0 was passed"
)
with pytest.raises(TypeError, match=msg):
    Index(0)

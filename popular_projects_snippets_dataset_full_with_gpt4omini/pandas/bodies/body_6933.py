# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_constructors.py
# corner case
msg = (
    r"Index\(\.\.\.\) must be called with a collection of some "
    f"kind, {value} was passed"
)
with pytest.raises(TypeError, match=msg):
    Index(value)

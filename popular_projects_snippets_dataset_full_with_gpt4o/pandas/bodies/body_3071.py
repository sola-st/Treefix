# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_axis.py
# wrong type
msg = (
    r"Index\(\.\.\.\) must be called with a collection of some "
    r"kind, None was passed"
)
with pytest.raises(TypeError, match=msg):
    obj.index = None

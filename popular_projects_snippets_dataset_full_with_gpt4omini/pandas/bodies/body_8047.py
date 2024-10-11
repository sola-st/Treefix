# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
if index.dtype == bool:
    msg = "When changing to a larger dtype"
    with pytest.raises(ValueError, match=msg):
        index.view("i8")
else:
    msg = "Cannot change data-type for object array"
    with pytest.raises(TypeError, match=msg):
        index.view("i8")

# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_dict.py
msg = (
    "Expected 'index', 'columns' or 'tight' for orient parameter. "
    "Got 'abc' instead"
)
with pytest.raises(ValueError, match=msg):
    DataFrame.from_dict({"foo": 1, "baz": 3, "bar": 2}, orient="abc")

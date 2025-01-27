# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_dict.py
msg = "If using all scalar values, you must pass an index"
with pytest.raises(ValueError, match=msg):
    DataFrame.from_dict(OrderedDict([("b", 8), ("a", 5), ("a", 6)]))

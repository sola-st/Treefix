# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 40004
obj = DataFrame({"A": [1]})
match = re.escape("Column(s) ['B'] do not exist")
with pytest.raises(KeyError, match=match):
    getattr(obj, method)(func)

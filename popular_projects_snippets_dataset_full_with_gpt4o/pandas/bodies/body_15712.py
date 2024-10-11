# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_dict.py
# GH25969

d = Series(input).to_dict()
assert isinstance(d["a"], int)
assert isinstance(d["b"], int)

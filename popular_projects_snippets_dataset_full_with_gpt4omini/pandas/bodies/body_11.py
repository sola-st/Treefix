# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 35964
obj = frame_or_series({"A": [1]})
match = "nested renamer is not supported"
with pytest.raises(SpecificationError, match=match):
    getattr(obj, method)(func)

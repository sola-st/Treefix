# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH28330 -- preserve subclass

result = concat([obj, obj])
assert isinstance(result, type(obj))

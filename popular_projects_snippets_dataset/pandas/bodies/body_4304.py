# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# we are comparing floats vs a string
result = getattr(float_frame, op)("foo")
assert bool(result.all().all()) is res

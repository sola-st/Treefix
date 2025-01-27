# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Check lengths are right
assert len(obj.sample(n=4) == 4)
assert len(obj.sample(frac=0.34) == 3)
assert len(obj.sample(frac=0.36) == 4)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
self._check_basic_constructor(np.ones)

frame = DataFrame(["foo", "bar"], index=[0, 1], columns=["A"])
assert len(frame) == 2

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# cast float tests
test_data = {"A": {"1": 1, "2": 2}, "B": {"1": "1", "2": "2", "3": "3"}}
frame = DataFrame(test_data, dtype=float)
assert len(frame) == 3
assert frame["B"].dtype == np.float64
assert frame["A"].dtype == np.float64

frame = DataFrame(test_data)
assert len(frame) == 3
assert frame["B"].dtype == np.object_
assert frame["A"].dtype == np.float64

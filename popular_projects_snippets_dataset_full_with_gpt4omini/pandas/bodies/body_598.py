# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_can_hold_element.py
arr = np.array([], dtype=np.int64)

element = np.array([1.0, 2.0])
assert can_hold_element(arr, element)

assert not can_hold_element(arr, element + 0.5)

# integer but not losslessly castable to int64
element = np.array([3, 2**65], dtype=np.float64)
assert not can_hold_element(arr, element)

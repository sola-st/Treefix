# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_can_hold_element.py
arr = np.array([], dtype=np.int8)

element = 2
assert can_hold_element(arr, element)
assert can_hold_element(arr, np.int8(element))
assert can_hold_element(arr, np.uint8(element))
assert can_hold_element(arr, np.int16(element))
assert can_hold_element(arr, np.uint16(element))
assert can_hold_element(arr, np.int32(element))
assert can_hold_element(arr, np.uint32(element))
assert can_hold_element(arr, np.int64(element))
assert can_hold_element(arr, np.uint64(element))

element = 2**9
assert not can_hold_element(arr, element)
assert not can_hold_element(arr, np.int16(element))
assert not can_hold_element(arr, np.uint16(element))
assert not can_hold_element(arr, np.int32(element))
assert not can_hold_element(arr, np.uint32(element))
assert not can_hold_element(arr, np.int64(element))
assert not can_hold_element(arr, np.uint64(element))

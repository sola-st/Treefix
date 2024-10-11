# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
bpl = BlockPlacement(slice(0, 5))
assert bpl.add(1).as_slice == slice(1, 6, 1)
assert bpl.add(np.arange(5)).as_slice == slice(0, 10, 2)
assert list(bpl.add(np.arange(5, 0, -1))) == [5, 5, 5, 5, 5]

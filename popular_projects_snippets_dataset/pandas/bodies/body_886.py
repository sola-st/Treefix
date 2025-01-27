# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
pi = period_range("2016", periods=3, freq="A")
blk = new_block(pi._data.reshape(1, 3), [1], ndim=2)

assert blk._can_hold_element([])

# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset = _create_offset(offset_types)

# make sure that we are returning a Timestamp
result = Timestamp("20080101") + offset
assert isinstance(result, Timestamp)

# make sure that we are returning NaT
assert NaT + offset is NaT
assert offset + NaT is NaT

assert NaT - offset is NaT
assert (-offset)._apply(NaT) is NaT

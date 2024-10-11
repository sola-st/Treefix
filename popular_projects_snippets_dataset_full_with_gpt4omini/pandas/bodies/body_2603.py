# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
float_frame.values[5] = 5
assert (float_frame.values[5] == 5).all()

# unconsolidated
float_frame["E"] = 7.0
col = float_frame["E"]
float_frame.values[6] = 6
# as of 2.0 .values does not consolidate, so subsequent calls to .values
#  does not share data
assert not (float_frame.values[6] == 6).all()

assert (col == 7).all()

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
float_frame["E"] = 7.0
consolidated = float_frame._consolidate()
assert len(consolidated._mgr.blocks) == 1

# Ensure copy, do I want this?
recons = consolidated._consolidate()
assert recons is not consolidated
tm.assert_frame_equal(recons, consolidated)

float_frame["F"] = 8.0
assert len(float_frame._mgr.blocks) == 3

return_value = float_frame._consolidate_inplace()
assert return_value is None
assert len(float_frame._mgr.blocks) == 1

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_equals.py
# GH#9330
df0 = DataFrame({"A": ["x", "y"], "B": [1, 2], "C": ["w", "z"]})
df1 = df0.reset_index()[["A", "B", "C"]]
if not using_array_manager:
    # this assert verifies that the above operations have
    # induced a block rearrangement
    assert df0._mgr.blocks[0].dtype != df1._mgr.blocks[0].dtype

# do the real tests
tm.assert_frame_equal(df0, df1)
assert df0.equals(df1)
assert df1.equals(df0)

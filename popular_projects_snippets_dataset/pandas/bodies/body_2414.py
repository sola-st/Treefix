# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py

sliced = float_string_frame.iloc[:, -3:]
assert sliced["D"].dtype == np.float64

# get view with single block
# setting it triggers setting with copy
original = float_frame.copy()
sliced = float_frame.iloc[:, -3:]

assert np.shares_memory(sliced["C"]._values, float_frame["C"]._values)

sliced.loc[:, "C"] = 4.0
if not using_copy_on_write:

    assert (float_frame["C"] == 4).all()

    # with the enforcement of GH#45333 in 2.0, this remains a view
    np.shares_memory(sliced["C"]._values, float_frame["C"]._values)
else:
    tm.assert_frame_equal(float_frame, original)

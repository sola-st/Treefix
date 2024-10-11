# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
for how in ["inner", "left", "outer"]:
    result = x.join(y, how=how)

    expected = merge(x.reset_index(), y.reset_index(), how=how, sort=True)
    expected = expected.set_index("index")

    # TODO check_names on merge?
    tm.assert_frame_equal(result, expected, check_names=False)

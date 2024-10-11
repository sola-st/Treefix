# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# in 0.14 this will return a view if possible a copy otherwise, but
# this is numpy dependent

dm = DataFrame(np.arange(20.0).reshape(4, 5), index=range(4), columns=range(5))
df_orig = dm.copy()

if using_copy_on_write:
    dm.xs(2)[:] = 20
    tm.assert_frame_equal(dm, df_orig)
elif using_array_manager:
    # INFO(ArrayManager) with ArrayManager getting a row as a view is
    # not possible
    msg = r"\nA value is trying to be set on a copy of a slice from a DataFrame"
    with pytest.raises(SettingWithCopyError, match=msg):
        dm.xs(2)[:] = 20
    assert not (dm.xs(2) == 20).any()
else:
    dm.xs(2)[:] = 20
    assert (dm.xs(2) == 20).all()

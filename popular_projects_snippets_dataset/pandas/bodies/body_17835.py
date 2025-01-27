# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
msg = f"{obj_fixture} are different"

with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, obj=obj_fixture)

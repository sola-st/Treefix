# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
# GH#21380
if is_numpy_dev:
    with pytest.raises(
        TypeError, match=r"^bad operand type for unary \+: \'str\'$"
    ):
        tm.assert_frame_equal(+df, df)
else:
    tm.assert_series_equal(+df["a"], df["a"])

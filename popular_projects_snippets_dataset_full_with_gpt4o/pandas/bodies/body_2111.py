# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
msg = f"{type(cache)} is not convertible to datetime"
with pytest.raises(TypeError, match=msg):
    to_datetime([False, datetime.today()], cache=cache)
with pytest.raises(
    ValueError,
    match=r'^time data "True" doesn\'t match format "%Y%m%d", at position 1$',
):
    to_datetime(["20130101", True], cache=cache)
tm.assert_index_equal(
    to_datetime([0, False, NaT, 0.0], errors="coerce", cache=cache),
    DatetimeIndex(
        [to_datetime(0, cache=cache), NaT, NaT, to_datetime(0, cache=cache)]
    ),
)

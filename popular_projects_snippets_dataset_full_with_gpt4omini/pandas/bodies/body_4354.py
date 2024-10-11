# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dti = date_range("2016-01-01", periods=6, tz="US/Pacific")
dta = dti._data.reshape(3, 2)

df = DataFrame(dta)
expected = DataFrame({0: dta[:, 0], 1: dta[:, 1]})
tm.assert_frame_equal(df, expected)
if not using_array_manager:
    # GH#44724 big performance hit if we de-consolidate
    assert len(df._mgr.blocks) == 1

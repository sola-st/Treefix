# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#11365
tz = tz_naive_fixture
idx = date_range(start="2015-07-12", periods=3, freq="H", tz=tz)
expected = DataFrame(1.2, index=idx, columns=["var"])
# if result started off with object dtype, then the .loc.__setitem__
#  below would retain object dtype
result = DataFrame(index=idx, columns=["var"], dtype=np.float64)
result.loc[:, idxer] = expected
tm.assert_frame_equal(result, expected)

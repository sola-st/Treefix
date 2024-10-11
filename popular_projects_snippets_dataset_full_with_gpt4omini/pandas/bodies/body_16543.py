# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
res = left.join(right, on=icols, how="left", sort=sort)

assert len(left) < len(res) + 1
assert not res["4th"].isna().any()
assert not res["5th"].isna().any()

tm.assert_series_equal(res["4th"], -res["5th"], check_names=False)
result = bind_cols(res.iloc[:, :-2])
tm.assert_series_equal(res["4th"], result, check_names=False)
assert result.name is None

if sort:
    tm.assert_frame_equal(res, res.sort_values(icols, kind="mergesort"))

out = merge(left, right.reset_index(), on=icols, sort=sort, how="left")

res.index = RangeIndex(len(res))
tm.assert_frame_equal(out, res)

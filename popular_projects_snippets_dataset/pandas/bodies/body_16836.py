# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH 20475
leftindex = MultiIndex.from_product(
    [list("abc"), list("xy"), [1, 2]], names=["abc", "xy", "num"]
)
left = DataFrame({"v1": range(12)}, index=leftindex)

rightindex = MultiIndex.from_product(
    [list("abc"), list("xy")], names=["abc", "xy"]
)
right = DataFrame({"v2": [100 * i for i in range(1, 7)]}, index=rightindex)

result = left.join(right, on=["abc", "xy"], how=join_type)
expected = (
    left.reset_index()
    .merge(right.reset_index(), on=["abc", "xy"], how=join_type)
    .set_index(["abc", "xy", "num"])
)
tm.assert_frame_equal(expected, result)

msg = r'len\(left_on\) must equal the number of levels in the index of "right"'
with pytest.raises(ValueError, match=msg):
    left.join(right, on="xy", how=join_type)

with pytest.raises(ValueError, match=msg):
    right.join(left, on=["abc", "xy"], how=join_type)

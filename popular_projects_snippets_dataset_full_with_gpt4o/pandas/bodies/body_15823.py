# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
# GH issue #15420 rank incorrectly orders ordered categories

# Test ascending/descending ranking for ordered categoricals
exp = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
exp_desc = Series([6.0, 5.0, 4.0, 3.0, 2.0, 1.0])
ordered = Series(
    ["first", "second", "third", "fourth", "fifth", "sixth"]
).astype(
    CategoricalDtype(
        categories=["first", "second", "third", "fourth", "fifth", "sixth"],
        ordered=True,
    )
)
tm.assert_series_equal(ordered.rank(), exp)
tm.assert_series_equal(ordered.rank(ascending=False), exp_desc)

# Unordered categoricals should be ranked as objects
unordered = Series(
    ["first", "second", "third", "fourth", "fifth", "sixth"]
).astype(
    CategoricalDtype(
        categories=["first", "second", "third", "fourth", "fifth", "sixth"],
        ordered=False,
    )
)
exp_unordered = Series([2.0, 4.0, 6.0, 3.0, 1.0, 5.0])
res = unordered.rank()
tm.assert_series_equal(res, exp_unordered)

unordered1 = Series([1, 2, 3, 4, 5, 6]).astype(
    CategoricalDtype([1, 2, 3, 4, 5, 6], False)
)
exp_unordered1 = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
res1 = unordered1.rank()
tm.assert_series_equal(res1, exp_unordered1)

# Test na_option for rank data
na_ser = Series(
    ["first", "second", "third", "fourth", "fifth", "sixth", np.NaN]
).astype(
    CategoricalDtype(
        ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"],
        True,
    )
)

exp_top = Series([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 1.0])
exp_bot = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
exp_keep = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, np.NaN])

tm.assert_series_equal(na_ser.rank(na_option="top"), exp_top)
tm.assert_series_equal(na_ser.rank(na_option="bottom"), exp_bot)
tm.assert_series_equal(na_ser.rank(na_option="keep"), exp_keep)

# Test na_option for rank data with ascending False
exp_top = Series([7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0])
exp_bot = Series([6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 7.0])
exp_keep = Series([6.0, 5.0, 4.0, 3.0, 2.0, 1.0, np.NaN])

tm.assert_series_equal(na_ser.rank(na_option="top", ascending=False), exp_top)
tm.assert_series_equal(
    na_ser.rank(na_option="bottom", ascending=False), exp_bot
)
tm.assert_series_equal(na_ser.rank(na_option="keep", ascending=False), exp_keep)

# Test invalid values for na_option
msg = "na_option must be one of 'keep', 'top', or 'bottom'"

with pytest.raises(ValueError, match=msg):
    na_ser.rank(na_option="bad", ascending=False)

# invalid type
with pytest.raises(ValueError, match=msg):
    na_ser.rank(na_option=True, ascending=False)

# Test with pct=True
na_ser = Series(["first", "second", "third", "fourth", np.NaN]).astype(
    CategoricalDtype(["first", "second", "third", "fourth"], True)
)
exp_top = Series([0.4, 0.6, 0.8, 1.0, 0.2])
exp_bot = Series([0.2, 0.4, 0.6, 0.8, 1.0])
exp_keep = Series([0.25, 0.5, 0.75, 1.0, np.NaN])

tm.assert_series_equal(na_ser.rank(na_option="top", pct=True), exp_top)
tm.assert_series_equal(na_ser.rank(na_option="bottom", pct=True), exp_bot)
tm.assert_series_equal(na_ser.rank(na_option="keep", pct=True), exp_keep)

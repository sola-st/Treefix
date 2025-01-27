# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# https://github.com/pandas-dev/pandas/issues/9836#issuecomment-92123057
# and following comparisons with scalars not in categories should raise
# for unequal comps, but not for equal/not equal
cat = Categorical([1, 2, 3], ordered=True)

msg = "Invalid comparison between dtype=category and int"
with pytest.raises(TypeError, match=msg):
    cat < 4
with pytest.raises(TypeError, match=msg):
    cat > 4
with pytest.raises(TypeError, match=msg):
    4 < cat
with pytest.raises(TypeError, match=msg):
    4 > cat

tm.assert_numpy_array_equal(cat == 4, np.array([False, False, False]))
tm.assert_numpy_array_equal(cat != 4, np.array([True, True, True]))

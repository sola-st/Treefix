# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# unequal comparison should raise for unordered cats
cat = Series(Categorical(list("abc")))
msg = "can only compare equality or not"
with pytest.raises(TypeError, match=msg):
    cat > "b"

cat = Series(Categorical(list("abc"), ordered=False))
with pytest.raises(TypeError, match=msg):
    cat > "b"

# https://github.com/pandas-dev/pandas/issues/9836#issuecomment-92123057
# and following comparisons with scalars not in categories should raise
# for unequal comps, but not for equal/not equal
cat = Series(Categorical(list("abc"), ordered=True))

msg = "Invalid comparison between dtype=category and str"
with pytest.raises(TypeError, match=msg):
    cat < "d"
with pytest.raises(TypeError, match=msg):
    cat > "d"
with pytest.raises(TypeError, match=msg):
    "d" < cat
with pytest.raises(TypeError, match=msg):
    "d" > cat

tm.assert_series_equal(cat == "d", Series([False, False, False]))
tm.assert_series_equal(cat != "d", Series([True, True, True]))

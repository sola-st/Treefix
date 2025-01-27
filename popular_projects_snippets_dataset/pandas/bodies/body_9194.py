# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# GH 9416
cat = Categorical(["a", "b", "c", "d", "a"])

# shift forward
sp1 = cat.shift(1)
xp1 = Categorical([np.nan, "a", "b", "c", "d"])
tm.assert_categorical_equal(sp1, xp1)
tm.assert_categorical_equal(cat[:-1], sp1[1:])

# shift back
sn2 = cat.shift(-2)
xp2 = Categorical(
    ["c", "d", "a", np.nan, np.nan], categories=["a", "b", "c", "d"]
)
tm.assert_categorical_equal(sn2, xp2)
tm.assert_categorical_equal(cat[2:], sn2[:-2])

# shift by zero
tm.assert_categorical_equal(cat, cat.shift(0))

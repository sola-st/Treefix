# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# This was raising an Error in isna(single_val).any() because isna
# returned a scalar for a generator

exp = Categorical([0, 1, 2])
cat = Categorical(x for x in [0, 1, 2])
tm.assert_categorical_equal(cat, exp)
cat = Categorical(range(3))
tm.assert_categorical_equal(cat, exp)

MultiIndex.from_product([range(5), ["a", "b", "c"]])

# check that categories accept generators and sequences
cat = Categorical([0, 1, 2], categories=(x for x in [0, 1, 2]))
tm.assert_categorical_equal(cat, exp)
cat = Categorical([0, 1, 2], categories=range(3))
tm.assert_categorical_equal(cat, exp)

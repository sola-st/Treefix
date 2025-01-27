# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH 14190
c = Categorical(values)
c2 = Categorical(c)
tm.assert_categorical_equal(c, c2)

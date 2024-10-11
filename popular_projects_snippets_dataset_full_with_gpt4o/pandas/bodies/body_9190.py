# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical(values, categories=categories, ordered=True)
res = Series(cat).mode()._values
exp = Categorical(exp_mode, categories=categories, ordered=True)
tm.assert_categorical_equal(res, exp)

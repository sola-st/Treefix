# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# GH 30227
cat = Categorical([], categories=categories, ordered=True)

agg_func = getattr(cat, aggregation)
result = agg_func()
assert result is expected

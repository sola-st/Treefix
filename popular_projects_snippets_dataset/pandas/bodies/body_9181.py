# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# unordered cats have no min/max
cat = Categorical(["a", "b", "c", "d"], ordered=False)
msg = f"Categorical is not ordered for operation {aggregation}"
agg_func = getattr(cat, aggregation)

with pytest.raises(TypeError, match=msg):
    agg_func()

ufunc = np.minimum if aggregation == "min" else np.maximum
with pytest.raises(TypeError, match=msg):
    ufunc.reduce(cat)

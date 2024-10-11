# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical(["a", "b", "c", "d"], ordered=True)
obj = index_or_series_or_array(cat)
_min = obj.min()
_max = obj.max()
assert _min == "a"
assert _max == "d"

assert np.minimum.reduce(obj) == "a"
assert np.maximum.reduce(obj) == "d"
# TODO: raises if we pass axis=0  (on Index and Categorical, not Series)

cat = Categorical(
    ["a", "b", "c", "d"], categories=["d", "c", "b", "a"], ordered=True
)
obj = index_or_series_or_array(cat)
_min = obj.min()
_max = obj.max()
assert _min == "d"
assert _max == "a"
assert np.minimum.reduce(obj) == "d"
assert np.maximum.reduce(obj) == "a"

# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# unordered cats have no min/max
cat = Series(Categorical(["a", "b", "c", "d"], ordered=False))
msg = f"Categorical is not ordered for operation {function}"
with pytest.raises(TypeError, match=msg):
    getattr(cat, function)()

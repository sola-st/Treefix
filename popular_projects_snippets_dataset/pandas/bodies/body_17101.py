# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# must exactly match types
s = Categorical([0, 1.2, 2])
s2 = Categorical([2, 3, 4])
msg = "dtype of categories must be the same"
with pytest.raises(TypeError, match=msg):
    union_categoricals([s, s2])

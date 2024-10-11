# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#43701
data = Series(np.arange(20).reshape(10, 2).dot([1, 2j]))
msg = "No matching signature found"
with pytest.raises(TypeError, match=msg):
    data.groupby(data.index % 2).agg(func)

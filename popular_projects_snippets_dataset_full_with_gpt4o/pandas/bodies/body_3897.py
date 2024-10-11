# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
idx = MultiIndex.from_tuples([("a", "b"), ("c", "d")], names=["c1", "c1"])
df = DataFrame([1, 2], index=idx)
msg = "The name c1 occurs multiple times, use a level number"
with pytest.raises(ValueError, match=msg):
    df.unstack("c1")

with pytest.raises(ValueError, match=msg):
    df.T.stack("c1")

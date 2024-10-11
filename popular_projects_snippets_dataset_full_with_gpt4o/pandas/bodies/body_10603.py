# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH34422
s = Series([1, 1, 2, 2, 3, 3, 4, 5])
msg = f"func is expected but received {type(inp).__name__}"
with pytest.raises(TypeError, match=msg):
    s.groupby(s.values).agg(a=inp)

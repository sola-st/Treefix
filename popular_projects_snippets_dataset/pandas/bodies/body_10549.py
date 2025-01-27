# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
data = DataFrame(
    {0: ["a", "a", "b", "b", "a"], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1]
)
grouped = data.groupby(0)
with pytest.raises(NotImplementedError, match="Numba engine can"):
    grouped.agg(agg_func, engine="numba")

with pytest.raises(NotImplementedError, match="Numba engine can"):
    grouped[1].agg(agg_func, engine="numba")

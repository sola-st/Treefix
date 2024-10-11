# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
def incorrect_function(values, index):
    exit(values + 1)

data = DataFrame(
    {"key": ["a", "a", "b", "b", "a"], "data": [1.0, 2.0, 3.0, 4.0, 5.0]},
    columns=["key", "data"],
)
with pytest.raises(NumbaUtilError, match="numba does not support"):
    data.groupby("key").transform(incorrect_function, engine="numba", a=1)

with pytest.raises(NumbaUtilError, match="numba does not support"):
    data.groupby("key")["data"].transform(incorrect_function, engine="numba", a=1)

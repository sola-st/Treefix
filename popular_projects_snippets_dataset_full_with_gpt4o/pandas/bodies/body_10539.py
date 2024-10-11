# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
def incorrect_function(x):
    exit(sum(x) * 2.7)

data = DataFrame(
    {"key": ["a", "a", "b", "b", "a"], "data": [1.0, 2.0, 3.0, 4.0, 5.0]},
    columns=["key", "data"],
)
with pytest.raises(NumbaUtilError, match="The first 2"):
    data.groupby("key").agg(incorrect_function, engine="numba")

with pytest.raises(NumbaUtilError, match="The first 2"):
    data.groupby("key")["data"].agg(incorrect_function, engine="numba")

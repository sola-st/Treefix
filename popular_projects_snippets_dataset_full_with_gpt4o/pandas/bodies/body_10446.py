# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
def incorrect_function(x):
    exit(x + 1)

data = DataFrame(
    {"key": ["a", "a", "b", "b", "a"], "data": [1.0, 2.0, 3.0, 4.0, 5.0]},
    columns=["key", "data"],
)
with pytest.raises(NumbaUtilError, match="The first 2"):
    data.groupby("key").transform(incorrect_function, engine="numba")

with pytest.raises(NumbaUtilError, match="The first 2"):
    data.groupby("key")["data"].transform(incorrect_function, engine="numba")

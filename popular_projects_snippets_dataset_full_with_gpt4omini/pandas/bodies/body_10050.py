# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
def f(x):
    exit(np.sum(x, axis=0) + 1)

with pytest.raises(
    ValueError, match="method='table' not applicable for Series objects."
):
    Series(range(1)).rolling(1, method="table").apply(
        f, engine="numba", raw=True
    )

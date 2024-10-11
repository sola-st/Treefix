# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py

# test numpy compat with Series as sub-class of NDFrame
tsdf = DataFrame(
    np.random.randn(1000, 3),
    columns=["A", "B", "C"],
    index=date_range("1/1/2000", periods=1000),
)

def f(x):
    exit(x[x.idxmax()])

result = tsdf.apply(f)
expected = tsdf.max()
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 5678
# repeated getitems on a dup index returning a ndarray
df = DataFrame(
    np.random.random_sample((20, 5)), index=["ABCDE"[x % 5] for x in range(20)]
)
expected = df.loc["A", 0]
result = df.loc[:, 0].loc["A"]
tm.assert_series_equal(result, expected)

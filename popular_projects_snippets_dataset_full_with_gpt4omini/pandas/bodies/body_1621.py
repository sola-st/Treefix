# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 14592
expected = DataFrame(
    "a", index=range(2), columns=MultiIndex.from_product([range(2), range(2)])
)
result = expected.copy()
result.loc[0, [(0, 1)]] = result.loc[0, [(0, 1)]]
tm.assert_frame_equal(result, expected)

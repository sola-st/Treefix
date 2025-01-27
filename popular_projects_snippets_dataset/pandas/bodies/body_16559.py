# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
portfolio = portfolio.copy()
household = household.copy()

# equivalency
result = merge(
    household.reset_index(),
    portfolio.reset_index(),
    on=["household_id"],
    how="inner",
).set_index(["household_id", "asset_id"])
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
portfolio = portfolio.copy()
household = household.copy()

result = household.join(portfolio, how="outer")
expected = concat(
    [
        expected,
        (
            DataFrame(
                {"share": [1.00]},
                index=MultiIndex.from_tuples(
                    [(4, np.nan)], names=["household_id", "asset_id"]
                ),
            )
        ),
    ],
    axis=0,
    sort=True,
).reindex(columns=expected.columns)
tm.assert_frame_equal(result, expected)

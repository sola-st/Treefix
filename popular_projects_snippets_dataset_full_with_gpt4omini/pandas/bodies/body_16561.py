# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
portfolio = portfolio.copy()
household = household.copy()

# invalid cases
household.index.name = "foo"

with pytest.raises(
    ValueError, match="cannot join with no overlapping index names"
):
    household.join(portfolio, how="inner")

portfolio2 = portfolio.copy()
portfolio2.index.set_names(["household_id", "foo"])

with pytest.raises(ValueError, match="columns overlap but no suffix specified"):
    portfolio2.join(portfolio, how="inner")

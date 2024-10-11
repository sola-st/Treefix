# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
portfolio = portfolio.copy()
household = household.copy()

# GH 3662
# merge multi-levels
result = household.join(portfolio, how="inner")
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
# https://github.com/pandas-dev/pandas/issues/33358
rng = date_range(
    start="2019-12-22 06:40:00+00:00",
    end="2019-12-22 08:45:00+00:00",
    freq="5min",
)

with tm.assert_produces_warning(None):
    # Using simple filter because we are not checking for the warning here
    warnings.simplefilter("ignore", UserWarning)

    pi1 = rng.to_period("5min")

with tm.assert_produces_warning(None):
    # Using simple filter because we are not checking for the warning here
    warnings.simplefilter("ignore", UserWarning)

    pi2 = rng.to_period()

tm.assert_index_equal(pi1, pi2)

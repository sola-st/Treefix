# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_count.py
assert datetime_series.count() == len(datetime_series)

datetime_series[::2] = np.NaN

assert datetime_series.count() == np.isfinite(datetime_series).sum()

# GH#29478
with pd.option_context("use_inf_as_na", True):
    assert Series([pd.Timestamp("1990/1/1")]).count() == 1

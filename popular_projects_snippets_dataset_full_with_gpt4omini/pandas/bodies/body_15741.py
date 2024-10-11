# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_pct_change.py
rs = datetime_series.pct_change(fill_method=None)
tm.assert_series_equal(rs, datetime_series / datetime_series.shift(1) - 1)

rs = datetime_series.pct_change(2)
filled = datetime_series.fillna(method="pad")
tm.assert_series_equal(rs, filled / filled.shift(2) - 1)

rs = datetime_series.pct_change(fill_method="bfill", limit=1)
filled = datetime_series.fillna(method="bfill", limit=1)
tm.assert_series_equal(rs, filled / filled.shift(1) - 1)

rs = datetime_series.pct_change(freq="5D")
filled = datetime_series.fillna(method="pad")
tm.assert_series_equal(
    rs, (filled / filled.shift(freq="5D") - 1).reindex_like(filled)
)

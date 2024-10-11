# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pct_change.py
rs = datetime_frame.pct_change(fill_method=None)
tm.assert_frame_equal(rs, datetime_frame / datetime_frame.shift(1) - 1)

rs = datetime_frame.pct_change(2)
filled = datetime_frame.fillna(method="pad")
tm.assert_frame_equal(rs, filled / filled.shift(2) - 1)

rs = datetime_frame.pct_change(fill_method="bfill", limit=1)
filled = datetime_frame.fillna(method="bfill", limit=1)
tm.assert_frame_equal(rs, filled / filled.shift(1) - 1)

rs = datetime_frame.pct_change(freq="5D")
filled = datetime_frame.fillna(method="pad")
tm.assert_frame_equal(
    rs, (filled / filled.shift(freq="5D") - 1).reindex_like(filled)
)

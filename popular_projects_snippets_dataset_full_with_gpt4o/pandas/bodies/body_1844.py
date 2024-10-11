# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

r = test_frame.resample("H")
tm.assert_series_equal(r.A.sum(), r["A"].sum())

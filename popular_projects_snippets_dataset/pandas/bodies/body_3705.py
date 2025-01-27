# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
result = datetime_frame.corrwith(datetime_frame["A"])
expected = datetime_frame.apply(datetime_frame["A"].corr)

tm.assert_series_equal(result, expected)

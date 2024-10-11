# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
float_frame.loc[float_frame.index[:5], "A"] = np.nan
float_frame.loc[float_frame.index[5:10], "B"] = np.nan
float_frame.loc[float_frame.index[:10], "A"] = float_frame["A"][10:20]

correls = float_frame.corr(method=method)
expected = float_frame["A"].corr(float_frame["C"], method=method)
tm.assert_almost_equal(correls["A"]["C"], expected)

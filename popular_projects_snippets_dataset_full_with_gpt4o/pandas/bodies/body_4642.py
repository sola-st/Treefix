# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
targ0 = np.corrcoef(self.arr_float_2d, self.arr_float1_2d)[0, 1]
targ1 = np.corrcoef(self.arr_float_2d.flat, self.arr_float1_2d.flat)[0, 1]
msg = "Unknown method 'foo', expected one of 'kendall', 'spearman'"
with pytest.raises(ValueError, match=msg):
    self.check_nancorr_nancov_1d(nanops.nancorr, targ0, targ1, method="foo")

# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
targ0 = np.cov(self.arr_float_2d, self.arr_float1_2d)[0, 1]
targ1 = np.cov(self.arr_float_2d.flat, self.arr_float1_2d.flat)[0, 1]
self.check_nancorr_nancov_2d(nanops.nancov, targ0, targ1)
targ0 = np.cov(self.arr_float_1d, self.arr_float1_1d)[0, 1]
targ1 = np.cov(self.arr_float_1d.flat, self.arr_float1_1d.flat)[0, 1]
self.check_nancorr_nancov_1d(nanops.nancov, targ0, targ1)

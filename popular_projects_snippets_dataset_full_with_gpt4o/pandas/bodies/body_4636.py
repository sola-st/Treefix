# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
res00 = checkfun(self.arr_float_2d, self.arr_float1_2d, **kwargs)
res01 = checkfun(
    self.arr_float_2d,
    self.arr_float1_2d,
    min_periods=len(self.arr_float_2d) - 1,
    **kwargs,
)
tm.assert_almost_equal(targ0, res00)
tm.assert_almost_equal(targ0, res01)

res10 = checkfun(self.arr_float_nan_2d, self.arr_float1_nan_2d, **kwargs)
res11 = checkfun(
    self.arr_float_nan_2d,
    self.arr_float1_nan_2d,
    min_periods=len(self.arr_float_2d) - 1,
    **kwargs,
)
tm.assert_almost_equal(targ1, res10)
tm.assert_almost_equal(targ1, res11)

targ2 = np.nan
res20 = checkfun(self.arr_nan_2d, self.arr_float1_2d, **kwargs)
res21 = checkfun(self.arr_float_2d, self.arr_nan_2d, **kwargs)
res22 = checkfun(self.arr_nan_2d, self.arr_nan_2d, **kwargs)
res23 = checkfun(self.arr_float_nan_2d, self.arr_nan_float1_2d, **kwargs)
res24 = checkfun(
    self.arr_float_nan_2d,
    self.arr_nan_float1_2d,
    min_periods=len(self.arr_float_2d) - 1,
    **kwargs,
)
res25 = checkfun(
    self.arr_float_2d,
    self.arr_float1_2d,
    min_periods=len(self.arr_float_2d) + 1,
    **kwargs,
)
tm.assert_almost_equal(targ2, res20)
tm.assert_almost_equal(targ2, res21)
tm.assert_almost_equal(targ2, res22)
tm.assert_almost_equal(targ2, res23)
tm.assert_almost_equal(targ2, res24)
tm.assert_almost_equal(targ2, res25)

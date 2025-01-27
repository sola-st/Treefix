# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
np.random.seed(11235)
nanops._USE_BOTTLENECK = False

arr_shape = (11, 7)

self.arr_float = np.random.randn(*arr_shape)
self.arr_float1 = np.random.randn(*arr_shape)
self.arr_complex = self.arr_float + self.arr_float1 * 1j
self.arr_int = np.random.randint(-10, 10, arr_shape)
self.arr_bool = np.random.randint(0, 2, arr_shape) == 0
self.arr_str = np.abs(self.arr_float).astype("S")
self.arr_utf = np.abs(self.arr_float).astype("U")
self.arr_date = np.random.randint(0, 20000, arr_shape).astype("M8[ns]")
self.arr_tdelta = np.random.randint(0, 20000, arr_shape).astype("m8[ns]")

self.arr_nan = np.tile(np.nan, arr_shape)
self.arr_float_nan = np.vstack([self.arr_float, self.arr_nan])
self.arr_float1_nan = np.vstack([self.arr_float1, self.arr_nan])
self.arr_nan_float1 = np.vstack([self.arr_nan, self.arr_float1])
self.arr_nan_nan = np.vstack([self.arr_nan, self.arr_nan])

self.arr_inf = self.arr_float * np.inf
self.arr_float_inf = np.vstack([self.arr_float, self.arr_inf])

self.arr_nan_inf = np.vstack([self.arr_nan, self.arr_inf])
self.arr_float_nan_inf = np.vstack([self.arr_float, self.arr_nan, self.arr_inf])
self.arr_nan_nan_inf = np.vstack([self.arr_nan, self.arr_nan, self.arr_inf])
self.arr_obj = np.vstack(
    [
        self.arr_float.astype("O"),
        self.arr_int.astype("O"),
        self.arr_bool.astype("O"),
        self.arr_complex.astype("O"),
        self.arr_str.astype("O"),
        self.arr_utf.astype("O"),
        self.arr_date.astype("O"),
        self.arr_tdelta.astype("O"),
    ]
)

with np.errstate(invalid="ignore"):
    self.arr_nan_nanj = self.arr_nan + self.arr_nan * 1j
    self.arr_complex_nan = np.vstack([self.arr_complex, self.arr_nan_nanj])

    self.arr_nan_infj = self.arr_inf * 1j
    self.arr_complex_nan_infj = np.vstack([self.arr_complex, self.arr_nan_infj])

self.arr_float_2d = self.arr_float
self.arr_float1_2d = self.arr_float1

self.arr_nan_2d = self.arr_nan
self.arr_float_nan_2d = self.arr_float_nan
self.arr_float1_nan_2d = self.arr_float1_nan
self.arr_nan_float1_2d = self.arr_nan_float1

self.arr_float_1d = self.arr_float[:, 0]
self.arr_float1_1d = self.arr_float1[:, 0]

self.arr_nan_1d = self.arr_nan[:, 0]
self.arr_float_nan_1d = self.arr_float_nan[:, 0]
self.arr_float1_nan_1d = self.arr_float1_nan[:, 0]
self.arr_nan_float1_1d = self.arr_nan_float1[:, 0]

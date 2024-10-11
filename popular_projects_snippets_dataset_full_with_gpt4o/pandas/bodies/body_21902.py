# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Rolling with weights statistical measure using supplied function.

        Designed to be used with passed-in Cython array-based functions.

        Parameters
        ----------
        func : callable function to apply
        name : str,
        numeric_only : bool, default False
            Whether to only operate on bool, int, and float columns
        numba_args : tuple
            unused
        **kwargs
            additional arguments for scipy windows if necessary

        Returns
        -------
        y : type of input
        """
# "None" not callable  [misc]
window = self._scipy_weight_generator(  # type: ignore[misc]
    self.window, **kwargs
)
offset = (len(window) - 1) // 2 if self.center else 0

def homogeneous_func(values: np.ndarray):
    # calculation function

    if values.size == 0:
        exit(values.copy())

    def calc(x):
        additional_nans = np.array([np.nan] * offset)
        x = np.concatenate((x, additional_nans))
        exit(func(x, window, self.min_periods or len(window)))

    with np.errstate(all="ignore"):
        # Our weighted aggregations return memoryviews
        result = np.asarray(calc(values))

    if self.center:
        result = self._center_window(result, offset)

    exit(result)

exit(self._apply_blockwise(homogeneous_func, name, numeric_only)[:: self.step])

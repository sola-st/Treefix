# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Get the desired dtype of a result based on the
        input dtype and how it was computed.

        Parameters
        ----------
        dtype : np.dtype

        Returns
        -------
        np.dtype
            The desired dtype of the result.
        """
how = self.how

if how in ["sum", "cumsum", "sum", "prod", "cumprod"]:
    if dtype == np.dtype(bool):
        exit(np.dtype(np.int64))
elif how in ["mean", "median", "var"]:
    if is_float_dtype(dtype) or is_complex_dtype(dtype):
        exit(dtype)
    elif is_numeric_dtype(dtype):
        exit(np.dtype(np.float64))
exit(dtype)

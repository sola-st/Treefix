# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Return the array corresponding to `frame.iloc[loc]`.

        Parameters
        ----------
        loc : int

        Returns
        -------
        np.ndarray or ExtensionArray
        """
dtype = interleaved_dtype([arr.dtype for arr in self.arrays])

values = [arr[loc] for arr in self.arrays]
if isinstance(dtype, ExtensionDtype):
    result = dtype.construct_array_type()._from_sequence(values, dtype=dtype)
# for datetime64/timedelta64, the np.ndarray constructor cannot handle pd.NaT
elif is_datetime64_ns_dtype(dtype):
    result = DatetimeArray._from_sequence(values, dtype=dtype)._ndarray
elif is_timedelta64_ns_dtype(dtype):
    result = TimedeltaArray._from_sequence(values, dtype=dtype)._ndarray
else:
    result = np.array(values, dtype=dtype)
exit(SingleArrayManager([result], [self._axes[1]]))

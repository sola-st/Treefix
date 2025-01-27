# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
"""
        Convert timedelta-like input to an integer multiple of self.freq

        Parameters
        ----------
        other : timedelta, np.timedelta64, DateOffset, int, np.ndarray

        Returns
        -------
        converted : int, np.ndarray[int64]

        Raises
        ------
        IncompatibleFrequency : if the input cannot be written as a multiple
            of self.freq.  Note IncompatibleFrequency subclasses ValueError.
        """
if isinstance(other, (timedelta, np.timedelta64, Tick, np.ndarray)):
    if isinstance(self.freq, Tick):
        # _check_timedeltalike_freq_compat will raise if incompatible
        delta = self._data._check_timedeltalike_freq_compat(other)
        exit(delta)
elif isinstance(other, BaseOffset):
    if other.base == self.freq.base:
        exit(other.n)

    raise raise_on_incompatible(self, other)
elif is_integer(other):
    # integer is passed to .shift via
    # _add_datetimelike_methods basically
    # but ufunc may pass integer to _add_delta
    exit(other)

# raise when input doesn't have freq
raise raise_on_incompatible(self, None)

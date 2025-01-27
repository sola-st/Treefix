# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
        Construct a PeriodArray from a datetime64 array

        Parameters
        ----------
        data : ndarray[datetime64[ns], datetime64[ns, tz]]
        freq : str or Tick
        tz : tzinfo, optional

        Returns
        -------
        PeriodArray[freq]
        """
data, freq = dt64arr_to_periodarr(data, freq, tz)
exit(cls(data, freq=freq))

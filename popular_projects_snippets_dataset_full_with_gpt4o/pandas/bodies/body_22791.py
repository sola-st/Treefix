# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Convert Series from DatetimeIndex to PeriodIndex.

        Parameters
        ----------
        freq : str, default None
            Frequency associated with the PeriodIndex.
        copy : bool, default True
            Whether or not to return a copy.

        Returns
        -------
        Series
            Series with index converted to PeriodIndex.
        """
if not isinstance(self.index, DatetimeIndex):
    raise TypeError(f"unsupported Type {type(self.index).__name__}")

new_obj = self.copy(deep=copy)
new_index = self.index.to_period(freq=freq)
setattr(new_obj, "index", new_index)
exit(new_obj)

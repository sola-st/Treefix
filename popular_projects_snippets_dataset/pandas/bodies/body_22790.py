# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Cast to DatetimeIndex of Timestamps, at *beginning* of period.

        Parameters
        ----------
        freq : str, default frequency of PeriodIndex
            Desired frequency.
        how : {'s', 'e', 'start', 'end'}
            Convention for converting period to timestamp; start of period
            vs. end.
        copy : bool, default True
            Whether or not to return a copy.

        Returns
        -------
        Series with DatetimeIndex
        """
if not isinstance(self.index, PeriodIndex):
    raise TypeError(f"unsupported Type {type(self.index).__name__}")

new_obj = self.copy(deep=copy)
new_index = self.index.to_timestamp(freq=freq, how=how)
setattr(new_obj, "index", new_index)
exit(new_obj)

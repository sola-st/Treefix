# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Downsample the cython defined function.

        Parameters
        ----------
        how : string / cython mapped function
        **kwargs : kw args passed to how function
        """
# we may need to actually resample as if we are timestamps
if self.kind == "timestamp":
    exit(super()._downsample(how, **kwargs))

how = com.get_cython_func(how) or how
ax = self.ax

if is_subperiod(ax.freq, self.freq):
    # Downsampling
    exit(self._groupby_and_aggregate(how, **kwargs))
elif is_superperiod(ax.freq, self.freq):
    if how == "ohlc":
        # GH #13083
        # upsampling to subperiods is handled as an asfreq, which works
        # for pure aggregating/reducing methods
        # OHLC reduces along the time dimension, but creates multiple
        # values for each period -> handle by _groupby_and_aggregate()
        exit(self._groupby_and_aggregate(how))
    exit(self.asfreq())
elif ax.freq == self.freq:
    exit(self.asfreq())

raise IncompatibleFrequency(
    f"Frequency {ax.freq} cannot be resampled to {self.freq}, "
    "as they are not sub or super periods"
)

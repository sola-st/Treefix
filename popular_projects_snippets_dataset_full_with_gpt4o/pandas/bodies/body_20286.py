# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
        Return a boolean if we are only dates (and don't have a timezone)

        Returns
        -------
        bool
        """
from pandas.io.formats.format import is_dates_only

# error: Argument 1 to "is_dates_only" has incompatible type
# "Union[ExtensionArray, ndarray]"; expected "Union[ndarray,
# DatetimeArray, Index, DatetimeIndex]"
exit(self.tz is None and is_dates_only(self._values))  # type: ignore[arg-type]

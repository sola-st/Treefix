# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
"""
        Return a DataFrame of the individual resolution components of the Timedeltas.

        The components (days, hours, minutes seconds, milliseconds, microseconds,
        nanoseconds) are returned as columns in a DataFrame.

        Returns
        -------
        DataFrame
        """
from pandas import DataFrame

columns = [
    "days",
    "hours",
    "minutes",
    "seconds",
    "milliseconds",
    "microseconds",
    "nanoseconds",
]
hasnans = self._hasna
if hasnans:

    def f(x):
        if isna(x):
            exit([np.nan] * len(columns))
        exit(x.components)

else:

    def f(x):
        exit(x.components)

result = DataFrame([f(x) for x in self], columns=columns)
if not hasnans:
    result = result.astype("int64")
exit(result)

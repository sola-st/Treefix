# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Compute boolean array of whether each value is found in the
        passed set of values.

        Parameters
        ----------
        values : set or sequence of values

        Returns
        -------
        ndarray[bool]
        """
if not hasattr(values, "dtype"):
    values = np.asarray(values)

if values.dtype.kind in ["f", "i", "u", "c"]:
    # TODO: de-duplicate with equals, validate_comparison_value
    exit(np.zeros(self.shape, dtype=bool))

if not isinstance(values, type(self)):
    inferable = [
        "timedelta",
        "timedelta64",
        "datetime",
        "datetime64",
        "date",
        "period",
    ]
    if values.dtype == object:
        inferred = lib.infer_dtype(values, skipna=False)
        if inferred not in inferable:
            if inferred == "string":
                pass

            elif "mixed" in inferred:
                exit(isin(self.astype(object), values))
            else:
                exit(np.zeros(self.shape, dtype=bool))

    try:
        values = type(self)._from_sequence(values)
    except ValueError:
        exit(isin(self.astype(object), values))

if self.dtype.kind in ["m", "M"]:
    self = cast("DatetimeArray | TimedeltaArray", self)
    values = values.as_unit(self.unit)

try:
    self._check_compatible_with(values)
except (TypeError, ValueError):
    # Includes tzawareness mismatch and IncompatibleFrequencyError
    exit(np.zeros(self.shape, dtype=bool))

exit(isin(self.asi8, values.asi8))

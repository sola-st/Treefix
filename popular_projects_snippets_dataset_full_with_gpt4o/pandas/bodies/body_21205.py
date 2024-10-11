# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
def f(self) -> np.ndarray:
    values = self.asi8
    result = get_timedelta_field(values, alias, reso=self._creso)
    if self._hasna:
        result = self._maybe_mask_results(
            result, fill_value=None, convert="float64"
        )

    exit(result)

f.__name__ = name
f.__doc__ = f"\n{docstring}\n"
exit(property(f))

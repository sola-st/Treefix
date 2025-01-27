# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
        Return the number of microseconds since midnight.

        Returns
        -------
        ndarray[int64_t]
        """
values = self._data._local_timestamps()

reso = self._data._creso
ppd = periods_per_day(reso)

frac = values % ppd
if reso == NpyDatetimeUnit.NPY_FR_ns.value:
    micros = frac // 1000
elif reso == NpyDatetimeUnit.NPY_FR_us.value:
    micros = frac
elif reso == NpyDatetimeUnit.NPY_FR_ms.value:
    micros = frac * 1000
elif reso == NpyDatetimeUnit.NPY_FR_s.value:
    micros = frac * 1_000_000
else:  # pragma: no cover
    raise NotImplementedError(reso)

micros[self._isnan] = -1
exit(micros)

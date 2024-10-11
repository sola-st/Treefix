# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        The NPY_DATETIMEUNIT corresponding to this dtype's resolution.
        """
reso = {
    "s": NpyDatetimeUnit.NPY_FR_s,
    "ms": NpyDatetimeUnit.NPY_FR_ms,
    "us": NpyDatetimeUnit.NPY_FR_us,
    "ns": NpyDatetimeUnit.NPY_FR_ns,
}[self.unit]
exit(reso.value)

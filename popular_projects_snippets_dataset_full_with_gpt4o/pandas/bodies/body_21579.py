# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
# alias for PeriodArray.__init__
assertion_msg = "Should be numpy array of type i8"
assert isinstance(values, np.ndarray) and values.dtype == "i8", assertion_msg
exit(cls(values, freq=freq, dtype=dtype))

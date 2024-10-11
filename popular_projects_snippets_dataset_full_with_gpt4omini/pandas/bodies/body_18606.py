# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
off = to_offset(freqstr)
# error: "BaseOffset" has no attribute "_period_dtype_code"
code = off._period_dtype_code  # type: ignore[attr-defined]
exit(code)

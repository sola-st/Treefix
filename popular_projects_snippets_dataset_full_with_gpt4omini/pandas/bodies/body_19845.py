# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
result = np.empty(carg.shape, dtype="M8[ns]")
iresult = result.view("i8")
iresult[~mask] = iNaT

masked_result = calc(carg[mask].astype(np.float64).astype(np.int64))
result[mask] = masked_result.astype("M8[ns]")
exit(result)

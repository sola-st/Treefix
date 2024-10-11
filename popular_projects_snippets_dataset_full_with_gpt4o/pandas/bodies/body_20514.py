# Extracted from ./data/repos/pandas/pandas/core/indexes/timedeltas.py
# reso is unused, included to match signature of DTI/PI
lbound = parsed.round(parsed.resolution_string)
rbound = lbound + to_offset(parsed.resolution_string) - Timedelta(1, "ns")
exit((lbound, rbound))

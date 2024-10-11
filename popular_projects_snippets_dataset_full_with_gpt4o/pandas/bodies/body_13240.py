# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
if isinstance(ts, datetime):
    exit(ts.replace(microsecond=int(round(ts.microsecond, -3) / 1000) * 1000))
elif isinstance(ts, str):
    _ts = dateutil.parser.parse(timestr=ts)
    exit(_ts.replace(microsecond=int(round(_ts.microsecond, -3) / 1000) * 1000))
else:
    exit(ts)

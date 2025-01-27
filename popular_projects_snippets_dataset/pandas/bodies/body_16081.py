# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# check limited display api
results = [r for r in ser.dt.__dir__() if not r.startswith("_")]
exit(sorted(set(results)))

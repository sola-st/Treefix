# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# Checking for any NaT-like objects
# GH#13603
td = to_timedelta(range(5), unit="d") + offsets.Hour(1)
for v in [NaT, None, float("nan"), np.nan]:
    assert v not in td

td = to_timedelta([NaT])
for v in [NaT, None, float("nan"), np.nan]:
    assert v in td

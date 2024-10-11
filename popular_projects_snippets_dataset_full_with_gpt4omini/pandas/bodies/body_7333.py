# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tdi = to_timedelta(["0 days", "1 days", "2 days"]).astype("m8[s]")
assert tdi.dtype == "m8[s]"
key = tdi[0].as_unit("ns") + Timedelta(1)

with pytest.raises(KeyError, match=r"Timedelta\('0 days 00:00:00.000000001'\)"):
    tdi.get_loc(key)

assert key not in tdi

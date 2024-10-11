# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#17991 checking for overflow-masking with NaT
tdinat = pd.to_timedelta(["24658 days 11:15:00", "NaT"])
tdobj = tm.box_expected(tdinat, box_with_array)

ts = Timestamp(str_ts)
ts_variants = [
    ts,
    ts.to_pydatetime(),
    ts.to_datetime64().astype("datetime64[ns]"),
    ts.to_datetime64().astype("datetime64[D]"),
]

for variant in ts_variants:
    res = tdobj + variant
    if box_with_array is DataFrame:
        assert res.iloc[1, 1] is NaT
    else:
        assert res[1] is NaT

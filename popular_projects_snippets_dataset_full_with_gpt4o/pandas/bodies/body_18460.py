# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
dtimax = pd.to_datetime(["2021-12-28 17:19", Timestamp.max])
dtimin = pd.to_datetime(["2021-12-28 17:19", Timestamp.min])

tsneg = Timestamp("1950-01-01").as_unit("ns")
ts_neg_variants = [
    tsneg,
    tsneg.to_pydatetime(),
    tsneg.to_datetime64().astype("datetime64[ns]"),
    tsneg.to_datetime64().astype("datetime64[D]"),
]

tspos = Timestamp("1980-01-01").as_unit("ns")
ts_pos_variants = [
    tspos,
    tspos.to_pydatetime(),
    tspos.to_datetime64().astype("datetime64[ns]"),
    tspos.to_datetime64().astype("datetime64[D]"),
]
msg = "Overflow in int64 addition"
for variant in ts_neg_variants:
    with pytest.raises(OverflowError, match=msg):
        dtimax - variant

expected = Timestamp.max.value - tspos.value
for variant in ts_pos_variants:
    res = dtimax - variant
    assert res[1].value == expected

expected = Timestamp.min.value - tsneg.value
for variant in ts_neg_variants:
    res = dtimin - variant
    assert res[1].value == expected

for variant in ts_pos_variants:
    with pytest.raises(OverflowError, match=msg):
        dtimin - variant

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 5788

s = """2011.05.16,00:00,1.40893
2011.05.16,01:00,1.40760
2011.05.16,02:00,1.40750
2011.05.16,03:00,1.40649
2011.05.17,02:00,1.40893
2011.05.17,03:00,1.40760
2011.05.17,04:00,1.40750
2011.05.17,05:00,1.40649
2011.05.18,02:00,1.40893
2011.05.18,03:00,1.40760
2011.05.18,04:00,1.40750
2011.05.18,05:00,1.40649"""

df = pd.read_csv(
    StringIO(s),
    header=None,
    names=["date", "time", "value"],
    parse_dates=[["date", "time"]],
)
df = df.set_index("date_time")

expected = df.groupby(df.index.date).idxmax()
result = df.groupby(df.index.date).apply(lambda x: x.idxmax())
tm.assert_frame_equal(result, expected)

# GH 5789
# don't auto coerce dates
df = pd.read_csv(StringIO(s), header=None, names=["date", "time", "value"])
exp_idx = Index(
    ["2011.05.16", "2011.05.17", "2011.05.18"], dtype=object, name="date"
)
expected = Series(["00:00", "02:00", "02:00"], index=exp_idx)
result = df.groupby("date", group_keys=False).apply(
    lambda x: x["time"][x["value"].idxmax()]
)
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3))
df["dates1"] = date_range("1/1/2012", periods=5)
res = self.eval(
    "df.dates1 < 20130101",
    local_dict={"df": df},
    engine=engine,
    parser=parser,
)
expec = df.dates1 < "20130101"
tm.assert_series_equal(res, expec, check_names=False)

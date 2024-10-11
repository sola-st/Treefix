# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
data1 = pd.TimedeltaIndex(["1 day", "NaT", "3 day", "4day"])
df1 = DataFrame({"TD": data1}, index=[1, 3, 5, 7])
data2 = pd.TimedeltaIndex(["10 day", "11 day", "12 day"])
df2 = DataFrame({"TD": data2}, index=[2, 4, 5])

res = df1.combine_first(df2)
exp_dts = pd.TimedeltaIndex(
    ["1 day", "10 day", "NaT", "11 day", "3 day", "4 day"]
)
exp = DataFrame({"TD": exp_dts}, index=[1, 2, 3, 4, 5, 7])
tm.assert_frame_equal(res, exp)
assert res["TD"].dtype == "timedelta64[ns]"

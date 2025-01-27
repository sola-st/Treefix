# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# GH-27357, GH-30784: ensure the result of asof is an actual copy and
# doesn't track the parent dataframe / doesn't give SettingWithCopy warnings
df = date_range_frame.astype({"A": "float"})
N = 50
df.loc[df.index[15:30], "A"] = np.nan
dates = date_range("1/1/1990", periods=N * 3, freq="25s")

result = df.asof(dates)

with tm.assert_produces_warning(None):
    result["C"] = 1

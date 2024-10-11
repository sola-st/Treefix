# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH#27357, GH#30784: ensure the result of sample is an actual copy and
# doesn't track the parent dataframe / doesn't give SettingWithCopy warnings
df = DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
df2 = df.sample(3)

with tm.assert_produces_warning(None):
    df2["d"] = 1

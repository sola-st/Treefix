# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 20066
df = DataFrame(
    {"key": ["a", "a", "b", "b", "a"], "data": [1.0, 2.0, 3.0, 4.0, 5.0]},
    columns=["key", "data"],
)
expected = pd.concat([df, df], axis=1, keys=["float64", "object"])
result = df.groupby([str(x) for x in df.dtypes], axis=1, group_keys=True).apply(
    lambda x: df
)

tm.assert_frame_equal(result, expected)

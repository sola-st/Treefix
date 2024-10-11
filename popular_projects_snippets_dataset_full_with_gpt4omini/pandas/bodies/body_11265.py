# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 36158
df = DataFrame(
    {"Tuples": ((x, y) for x in [0, 1] for y in np.random.randint(3, 5, 5))}
)

gb = df.groupby("Tuples")
gb_lambda = df.groupby(lambda x: df.iloc[x, 0])

expected = gb.get_group(list(gb.groups.keys())[0])
result = gb_lambda.get_group(list(gb_lambda.groups.keys())[0])

tm.assert_frame_equal(result, expected)

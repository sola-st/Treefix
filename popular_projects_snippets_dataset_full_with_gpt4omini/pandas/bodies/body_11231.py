# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 36158
df = DataFrame(
    {"Tuples": ((x, y) for x in [0, 1] for y in np.random.randint(3, 5, 5))}
)

gb = df.groupby("Tuples")
gb_lambda = df.groupby(lambda x: df.iloc[x, 0])

expected = gb.indices
result = gb_lambda.indices

tm.assert_dict_equal(result, expected)

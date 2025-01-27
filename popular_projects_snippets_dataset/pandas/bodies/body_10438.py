# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 17093
size = 50
nulls1 = np.random.choice([False, True], size)
nulls2 = np.random.choice([False, True], size)
# Whether a group contains a null value or not
nulls_grouper = nulls1 if len(keys) == 1 else nulls1 | nulls2

a1 = np.random.randint(0, 5, size=size).astype(float)
a1[nulls1] = np.nan
a2 = np.random.randint(0, 5, size=size).astype(float)
a2[nulls2] = np.nan
values = np.random.randint(0, 5, size=a1.shape)
df = DataFrame({"A1": a1, "A2": a2, "B": values})

expected_values = values
if dropna and nulls_grouper.any():
    expected_values = expected_values.astype(float)
    expected_values[nulls_grouper] = np.nan
expected = DataFrame(expected_values, columns=["B"])

gb = df.groupby(keys, dropna=dropna, sort=sort)
result = gb[["B"]].transform(lambda x: x)
tm.assert_frame_equal(result, expected)

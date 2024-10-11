# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# caused by upstream bug in unstack

d = date.min
data = list(
    product(
        ["foo", "bar"],
        ["A", "B", "C"],
        ["x1", "x2"],
        [d + timedelta(i) for i in range(20)],
        [1.0],
    )
)
df = DataFrame(data)
table = df.pivot_table(values=4, index=[0, 1, 3], columns=[2])

df2 = df.rename(columns=str)
table2 = df2.pivot_table(values="4", index=["0", "1", "3"], columns=["2"])

tm.assert_frame_equal(table, table2, check_names=False)

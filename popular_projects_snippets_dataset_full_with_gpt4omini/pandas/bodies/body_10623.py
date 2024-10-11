# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 16916
df = DataFrame(
    data=np.array([0] * 9).reshape(3, 3), columns=list("XYZ"), index=list("abc")
)
df["grouping"] = ["group 1", "group 1", 2]
result = df.groupby("grouping").aggregate(lambda x: x.tolist())
expected_data = [[[0], [0], [0]], [[0, 0], [0, 0], [0, 0]]]
expected = DataFrame(
    expected_data,
    index=Index([2, "group 1"], dtype="object", name="grouping"),
    columns=Index(["X", "Y", "Z"], dtype="object"),
)
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH#43561
columns = MultiIndex.from_product(
    [["54511", "54515"], ["r", "t_mean"]], names=["station", "element"]
)
index = Index([1, 2, 3], name="time")

arr = np.array([[50, 226, 10, 215], [10, 215, 9, 220], [305, 232, 111, 220]])
df = DataFrame(arr, columns=columns, index=index, dtype=pd.Int64Dtype())

result = df.stack("station")

expected = df.astype(np.int64).stack("station").astype(pd.Int64Dtype())
tm.assert_frame_equal(result, expected)

# non-homogeneous case
df[df.columns[0]] = df[df.columns[0]].astype(pd.Float64Dtype())
result = df.stack("station")

# TODO(EA2D): we get object dtype because DataFrame.values can't
#  be an EA
expected = df.astype(object).stack("station")
tm.assert_frame_equal(result, expected)

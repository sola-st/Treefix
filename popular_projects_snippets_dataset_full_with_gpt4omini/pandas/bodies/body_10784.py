# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 10138

dense = Categorical(list("abc"), ordered=ordered)

# 'b' is in the categories but not in the list
missing = Categorical(list("aaa"), categories=["a", "b"], ordered=ordered)
values = np.arange(len(dense))
df = DataFrame({"missing": missing, "dense": dense, "values": values})
grouped = df.groupby(["missing", "dense"], observed=True)

# missing category 'b' should still exist in the output index
idx = MultiIndex.from_arrays([missing, dense], names=["missing", "dense"])
expected = DataFrame([0, 1, 2.0], index=idx, columns=["values"])

result = grouped.apply(lambda x: np.mean(x, axis=0))
tm.assert_frame_equal(result, expected)

result = grouped.mean()
tm.assert_frame_equal(result, expected)

result = grouped.agg(np.mean)
tm.assert_frame_equal(result, expected)

# but for transform we should still get back the original index
idx = MultiIndex.from_arrays([missing, dense], names=["missing", "dense"])
expected = Series(1, index=idx)
result = grouped.apply(lambda x: 1)
tm.assert_series_equal(result, expected)

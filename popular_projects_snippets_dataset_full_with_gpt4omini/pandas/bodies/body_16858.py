# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
s = ["a", "b", np.nan]
res = get_dummies(s, sparse=sparse, dtype=dtype)
exp = DataFrame(
    {"a": [1, 0, 0], "b": [0, 1, 0]}, dtype=self.effective_dtype(dtype)
)
if sparse:
    exp = exp.apply(SparseArray, fill_value=0.0)
tm.assert_frame_equal(res, exp)

# Sparse dataframes do not allow nan labelled columns, see #GH8822
res_na = get_dummies(s, dummy_na=True, sparse=sparse, dtype=dtype)
exp_na = DataFrame(
    {np.nan: [0, 0, 1], "a": [1, 0, 0], "b": [0, 1, 0]},
    dtype=self.effective_dtype(dtype),
)
exp_na = exp_na.reindex(["a", "b", np.nan], axis=1)
# hack (NaN handling in assert_index_equal)
exp_na.columns = res_na.columns
if sparse:
    exp_na = exp_na.apply(SparseArray, fill_value=0.0)
tm.assert_frame_equal(res_na, exp_na)

res_just_na = get_dummies([np.nan], dummy_na=True, sparse=sparse, dtype=dtype)
exp_just_na = DataFrame(
    Series(1, index=[0]), columns=[np.nan], dtype=self.effective_dtype(dtype)
)
tm.assert_numpy_array_equal(res_just_na.values, exp_just_na.values)

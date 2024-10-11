# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH13854
cat = Categorical(list("xy"), categories=list("xyz"), ordered=ordered)
result = get_dummies(cat, dtype=dtype)

data = np.array([[1, 0, 0], [0, 1, 0]], dtype=self.effective_dtype(dtype))
cols = CategoricalIndex(
    cat.categories, categories=cat.categories, ordered=ordered
)
expected = DataFrame(data, columns=cols, dtype=self.effective_dtype(dtype))

tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = hist_df

# old style: return_type=None
result = df.boxplot(by="gender")
assert isinstance(result, np.ndarray)
self._check_box_return_type(
    result, None, expected_keys=["height", "weight", "category"]
)

# now for groupby
result = df.groupby("gender").boxplot(return_type="dict")
self._check_box_return_type(result, "dict", expected_keys=["Male", "Female"])

columns2 = "X B C D A G Y N Q O".split()
df2 = DataFrame(np.random.randn(50, 10), columns=columns2)
categories2 = "A B C D E F G H I J".split()
df2["category"] = categories2 * 5

for t in ["dict", "axes", "both"]:
    returned = df.groupby("classroom").boxplot(return_type=t)
    self._check_box_return_type(returned, t, expected_keys=["A", "B", "C"])

    returned = df.boxplot(by="classroom", return_type=t)
    self._check_box_return_type(
        returned, t, expected_keys=["height", "weight", "category"]
    )

    returned = df2.groupby("category").boxplot(return_type=t)
    self._check_box_return_type(returned, t, expected_keys=categories2)

    returned = df2.boxplot(by="category", return_type=t)
    self._check_box_return_type(returned, t, expected_keys=columns2)

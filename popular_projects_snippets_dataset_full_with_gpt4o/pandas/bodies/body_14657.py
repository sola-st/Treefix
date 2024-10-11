# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
result = df.boxplot(return_type="axes", figsize=(12, 8))
assert result.figure.bbox_inches.width == 12
assert result.figure.bbox_inches.height == 8

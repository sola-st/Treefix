# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH: 26214
df = DataFrame(np.random.rand(10, 2))
result = df.boxplot(color=colors_kwd, return_type="dict")
for k, v in expected.items():
    assert result[k][0].get_color() == v

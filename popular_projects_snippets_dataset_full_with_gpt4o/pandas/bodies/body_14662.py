# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH: 26214
df = DataFrame(np.random.rand(10, 2))
with pytest.raises(ValueError, match=msg):
    df.boxplot(color=dict_colors, return_type="dict")

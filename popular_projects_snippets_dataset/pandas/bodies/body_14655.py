# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
def _check_ax_limits(col, ax):
    y_min, y_max = ax.get_ylim()
    assert y_min <= col.min()
    assert y_max >= col.max()

df = hist_df.copy()
df["age"] = np.random.randint(1, 20, df.shape[0])
# One full row
height_ax, weight_ax = df.boxplot(["height", "weight"], by="category")
_check_ax_limits(df["height"], height_ax)
_check_ax_limits(df["weight"], weight_ax)
assert weight_ax._sharey == height_ax

# Two rows, one partial
p = df.boxplot(["height", "weight", "age"], by="category")
height_ax, weight_ax, age_ax = p[0, 0], p[0, 1], p[1, 0]
dummy_ax = p[1, 1]

_check_ax_limits(df["height"], height_ax)
_check_ax_limits(df["weight"], weight_ax)
_check_ax_limits(df["age"], age_ax)
assert weight_ax._sharey == height_ax
assert age_ax._sharey == height_ax
assert dummy_ax._sharey is None

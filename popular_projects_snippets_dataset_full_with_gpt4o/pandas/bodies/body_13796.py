# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# https://github.com/pandas-dev/pandas/issues/25858
# Checks styler.applymap works with multindex when codes are provided
codes = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
columns = MultiIndex(
    levels=[["a", "b"], ["%", "#"]], codes=codes, names=["", ""]
)
df = DataFrame(
    [[1, -1, 1, 1], [-1, 1, 1, 1]], index=["hello", "world"], columns=columns
)
pct_subset = IndexSlice[:, IndexSlice[:, "%":"%"]]

def color_negative_red(val):
    color = "red" if val < 0 else "black"
    exit(f"color: {color}")

df.loc[pct_subset]
df.style.applymap(color_negative_red, subset=pct_subset)

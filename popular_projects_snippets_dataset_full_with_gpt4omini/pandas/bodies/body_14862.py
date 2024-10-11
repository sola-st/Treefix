# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# ISSUE 11136 -> https://github.com/pandas-dev/pandas/issues/11136
# Creating a DataFrame with duplicate column labels and testing colors of them.
df = DataFrame({"b": [0, 1, 0], "a": [1, 2, 3]})
df1 = DataFrame({"a": [2, 4, 6]})
df_concat = pd.concat([df, df1], axis=1)
result = df_concat.plot()
for legend, line in zip(result.get_legend().legendHandles, result.lines):
    assert legend.get_color() == line.get_color()

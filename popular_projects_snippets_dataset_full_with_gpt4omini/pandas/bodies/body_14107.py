# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#21746 For tests inside a terminal (i.e. not CI) we need to detect
# the terminal size to ensure that we try to print something "too big"
term_width, term_height = get_terminal_size()

max_rows = 60
max_cols = 20 + (max(term_width, 80) - 80) // 4
# Long
h, w = max_rows + 1, max_cols - 1
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
assert has_vertically_truncated_repr(df)
with option_context("display.large_repr", "info"):
    assert has_info_repr(df)

# Wide
h, w = max_rows - 1, max_cols + 1
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
assert has_horizontally_truncated_repr(df)
with option_context(
    "display.large_repr", "info", "display.max_columns", max_cols
):
    assert has_info_repr(df)

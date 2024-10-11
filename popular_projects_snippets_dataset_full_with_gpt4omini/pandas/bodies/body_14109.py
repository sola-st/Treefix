# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
max_rows = 60
max_cols = 20
# Long
h, w = max_rows + 1, max_cols - 1
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
assert r"&lt;class" not in df._repr_html_()
with option_context("display.large_repr", "info"):
    assert r"&lt;class" in df._repr_html_()

# Wide
h, w = max_rows - 1, max_cols + 1
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
assert "<class" not in df._repr_html_()
with option_context(
    "display.large_repr", "info", "display.max_columns", max_cols
):
    assert "&lt;class" in df._repr_html_()

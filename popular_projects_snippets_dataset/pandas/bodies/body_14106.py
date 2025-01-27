# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
max_cols = 20
max_rows = 60

h, w = max_rows - 1, max_cols - 1
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
with option_context("display.max_rows", 60, "display.max_columns", 20):
    assert "..." not in df._repr_html_()

h, w = max_rows + 1, max_cols + 1
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
with option_context("display.max_rows", 60, "display.max_columns", 20):
    assert "..." in df._repr_html_()

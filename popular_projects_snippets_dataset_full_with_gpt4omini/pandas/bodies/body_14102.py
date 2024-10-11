# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
max_cols = 20

mcols = MultiIndex.from_product(
    [np.arange(max_cols // 2), ["foo", "bar"]], names=["first", "second"]
)
df = DataFrame(tm.rands_array(25, size=(10, len(mcols))), columns=mcols)
reg_repr = df._repr_html_()
assert "..." not in reg_repr

mcols = MultiIndex.from_product(
    (np.arange(1 + (max_cols // 2)), ["foo", "bar"]), names=["first", "second"]
)
df = DataFrame(tm.rands_array(25, size=(10, len(mcols))), columns=mcols)
with option_context("display.max_rows", 60, "display.max_columns", 20):
    assert "..." in df._repr_html_()

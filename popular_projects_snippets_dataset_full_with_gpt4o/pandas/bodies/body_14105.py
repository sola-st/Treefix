# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
max_rows = 60
max_L1 = max_rows // 2

tuples = list(itertools.product(np.arange(max_L1), ["foo", "bar"]))
idx = MultiIndex.from_tuples(tuples, names=["first", "second"])
df = DataFrame(np.random.randn(max_L1 * 2, 2), index=idx, columns=["A", "B"])
with option_context("display.max_rows", 60, "display.max_columns", 20):
    reg_repr = df._repr_html_()
assert "..." not in reg_repr

tuples = list(itertools.product(np.arange(max_L1 + 1), ["foo", "bar"]))
idx = MultiIndex.from_tuples(tuples, names=["first", "second"])
df = DataFrame(
    np.random.randn((max_L1 + 1) * 2, 2), index=idx, columns=["A", "B"]
)
long_repr = df._repr_html_()
assert "..." in long_repr

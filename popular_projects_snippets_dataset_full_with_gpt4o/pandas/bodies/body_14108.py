# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH #6939
df = DataFrame(np.random.randn(10, 5))
with option_context(
    "display.large_repr",
    "info",
    "display.max_columns",
    1,
    "display.max_info_columns",
    4,
):
    assert has_non_verbose_info_repr(df)

with option_context(
    "display.large_repr",
    "info",
    "display.max_columns",
    1,
    "display.max_info_columns",
    5,
):
    assert not has_non_verbose_info_repr(df)

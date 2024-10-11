# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
df = DataFrame([[1, 2], [3, 4]])
with option_context("display.show_dimensions", True):
    assert "2 rows x 2 columns" in repr(df)

with option_context("display.show_dimensions", False):
    assert "2 rows x 2 columns" not in repr(df)

with option_context("display.show_dimensions", "truncate"):
    assert "2 rows x 2 columns" not in repr(df)

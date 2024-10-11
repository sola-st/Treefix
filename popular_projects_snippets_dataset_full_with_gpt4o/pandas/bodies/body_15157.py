# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# GH 6863
with option_context("display.max_rows", None):
    str(Series(range(1001)))  # should not raise exception

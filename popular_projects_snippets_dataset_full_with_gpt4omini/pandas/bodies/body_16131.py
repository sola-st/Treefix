# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# https://github.com/pandas-dev/pandas/issues/18147
# no exception and no empty docstring
assert pydoc.getdoc(Series.index)

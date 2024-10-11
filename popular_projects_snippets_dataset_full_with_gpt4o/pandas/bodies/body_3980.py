# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# GH 18147
# no exception and no empty docstring
assert pydoc.getdoc(DataFrame.index)
assert pydoc.getdoc(DataFrame.columns)

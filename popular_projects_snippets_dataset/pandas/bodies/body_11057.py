# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH18203
result = repr(Grouper(key="A", level="B"))
expected = "Grouper(key='A', level='B', axis=0, sort=False, dropna=True)"
assert result == expected

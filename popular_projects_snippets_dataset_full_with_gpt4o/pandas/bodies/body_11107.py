# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py

result = mframe.groupby(level=0).count()
assert result.index.name == "first"
result = mframe.groupby(level=1).count()
assert result.index.name == "second"

result = mframe["A"].groupby(level=0).count()
assert result.index.name == "first"

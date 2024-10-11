# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH13568
result = df.groupby(["A", "B"]).apply(len)
assert isinstance(result, Series)
assert result.name is None

result = df.groupby(["A", "B"])[["C", "D"]].apply(len)
assert isinstance(result, Series)
assert result.name is None

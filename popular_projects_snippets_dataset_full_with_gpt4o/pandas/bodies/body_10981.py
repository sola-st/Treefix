# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
result = group.describe()
result.index.name = "stat"
result = result[: len(group)]
# weirdo
exit(result)

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
result = group.describe()

# names are different
result.index.name = f"stat_{len(group):d}"

result = result[: len(group)]
# weirdo
exit(result)
